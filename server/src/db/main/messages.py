from dataclasses import dataclass
from ..db_utils import exec_get_all, exec_sql_file, exec_commit, exec_get_one

@dataclass
class Message:
    message_id: str
    user_id: str
    msg_body: str
    is_deleted: bool
    
def rebuild_bet_tables():
    exec_sql_file("src/db/sql/message.sql")

def list_messages():
    """
    List off messages made in server
    """
    list_msg = """
        SELECT *
        FROM Messages;
    """
    res = exec_get_all(list_msg)
    return res if res else []

def create_message(user_id, msg_body):
    """
    Writes a new message onto the system
    """
    create_message = """
            INSERT INTO Messages
            (user_id, msg_body)
            VALUES (%s, %s)
            RETURNING message_id;
        """
    exec_commit(create_message, (user_id, msg_body))

    return {"message": "message created successfully"}

def get_message(message_id):
    """
    grabs message details by message ID
    """
    select_message_sql = """
            SELECT * FROM Messages WHERE message_id = %s;
        """
    res = exec_get_one(select_message_sql, (message_id))
    return res if res else []

def delete_message(message_id):
    """
    MODS ONLY: deletes message from table
    """
    delete_message_sql = """
            UPDATE Messages
            SET is_deleted = true
            WHERE message_id = %s;
        """
    exec_commit(delete_message_sql, (message_id))
    return {"message": "message deleted successfully"}