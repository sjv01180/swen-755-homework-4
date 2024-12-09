from ..db_utils import exec_get_all, exec_sql_file, exec_commit, exec_get_one
import datetime as dt
import re
import secrets
import hashlib

def rebuild_user_tables():
    exec_sql_file("src/db/sql/user.sql")
    exec_sql_file("src/db/sql/userData.sql")


def recreate_user_table():
    """
    recreate user table if need
    """
    rebuild_user_tables()

def clear_users():
    """
    clear users data
    """
    sql = "delete from users"
    exec_commit(sql)

class User:
    """
    class for user
    """
    def __init__(self, uid: str, username: str, is_mod: bool = False):
        """
        constructor
        :param username:
        """
        if username is None:
            raise ValueError

        self.uid = uid
        self.username = username.strip()
        self.is_mod = is_mod

        if len(self.username) == 0:
            raise ValueError

    def to_json(self):
        return {"username": self.username}
    
def _hash_string(input: str) -> str:
    """
    internal helper function to salt and hash strings. Eliminates DRY and localizes salting algorithm in one place
    :param input:
    :return: hashed variant of string
    """
    newpass = hashlib.sha512()
    newpass.update(b"Marco")
    newpass.update(input.encode())
    newpass.update(b"Pollo")
    return newpass.hexdigest()


def _get_user_by_session(session: str) -> User:
    """
    get user by session id
    :param session:
    :return: user
    """
    select_sql = "SELECT user_id, user_name, is_mod FROM users WHERE session_id = %s"
    res = exec_get_one(select_sql, (session,))
    if res is None:
        return res
    return User(res[0], res[1], res[2])

def _get_user_by_username(username: str) -> User:
    """
    get user by username
    :param username:
    :return: user
    """
    # Added is_deleted param to returning user object. 
    # Not sure how we want to handle deleted users, but I think we can add some sort of special label to the frontend or something
    select_sql = "SELECT user_id, user_name, is_mod FROM users WHERE user_name = %s"
    res = exec_get_one(select_sql, (username,))
    if res is None:
        return res

    return User(res[0], res[1], res[2])

def _cancel_session_by_uid(uid: str) -> bool:
    """
    removes session from user by username
    :param uid:
    """

    # might be redundant and may replace matching from username to session id. Let me know in the pull request feedback
    update_sql = "UPDATE users SET session_id = NULL WHERE user_id = %s"
    exec_commit(update_sql, (uid,))
    return True

#========PUBLIC USER FUNCTIONS==========

def create_user(user: User, password: str) -> bool:
    """
    create a new account
    :param user:
    :param password
    :return: True if create success
    """
    if _get_user_by_username(user.username) is not None:
        return False
    
    hashed_pass = _hash_string(password)
    insert_sql = """
        INSERT INTO users (user_name, password) VALUES (%s, %s)
    """
    exec_commit(insert_sql, (user.username, hashed_pass,))
    return True

def validate_user(username: str, password: str) -> bool:
    """
    checks if username and password points to a valid account
    :param username:
    :param password:
    :return: True if username and password is valid, False otherwise
    """
    cur_user = _get_user_by_username(username)
    if cur_user is None:
        return False
    hashed_pass = _hash_string(password)
    validate_sql = "SELECT user_name FROM users WHERE user_id = %s AND password = %s"
    user_status = exec_get_one(validate_sql, (cur_user.uid, hashed_pass,))
    if user_status is None:
        return False
    return True

def invalidate_user(session: str) -> bool:
    """
    destroy auth session of user for logging off
    :param username:
    :param session:
    :return: True if session destroyed successfully, false otherwise
    """
    cur_user = _get_user_by_session(session)
    if cur_user is None:
        return False
    return _cancel_session_by_uid(cur_user.uid)

def get_user(username: str, session: str) -> User | None:
    """
    Finds user by username. Public rendition of _get_user_by_username
    :param username:
    :param session:
    :return: user
    """
    print(session)
    if session is None:
        return None
    cur_user = _get_user_by_session(session)
    if cur_user is None:
        return None
    return _get_user_by_username(username)

def update_user_session_id(username: str) -> str:
    """
    update user session_id
    """
    session_id = secrets.token_hex(128)
    update_sql = "UPDATE users SET session_id = %s WHERE user_name = %s"
    exec_commit(update_sql, (session_id, username))
    update_sql = "UPDATE users SET last_login = NOW() WHERE user_name = %s"
    exec_commit(update_sql, (username,))
    return session_id

# REFACTORED BREAKER - SESSION EXPIRATION MANAGEMENT (Backend Helper Function)
def check_session_expiration(session: str) -> bool:
    """
    internal helper function to compare dates between user's last login and today. If the session lasts longer than a day, then it is expired
    :param session:
    :return: true if session is considered expired, false otherwise
    """
    select_sql = "SELECT last_login FROM users WHERE session_id = %s"
    res = exec_get_one(select_sql, (session,))
    login_date = res[0]
    time_diff = dt.datetime.now().date() - login_date
    return time_diff.days > 0
    

# recreate_user_table()