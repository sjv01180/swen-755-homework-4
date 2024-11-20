from ..db_utils import exec_get_all, exec_sql_file, exec_commit, exec_get_one
    
def recreate_message_table():
    exec_sql_file("src/db/sql/message.sql")
    exec_sql_file("src/db/sql/messageData.sql")

    
def clear_messages():
    """
    clear users data
    """
    sql = "delete from messages"
    exec_commit(sql)

def list_messages():
    """
    List off messages made in server
    """
    list_msg = """
        SELECT * FROM messages;
    """
    res = exec_get_all(list_msg)
    if res is None:
        return []
    return [dict(message_id=item[0], user_id=item[1], user_name=item[2], message=item[3], is_deleted=item[4]) for item in res]

def create_message(user_id, user_name, msg_body):
    """
    Writes a new message onto the system
    """
    create_message = """
            INSERT INTO messages
            (user_id, user_name, msg_body)
            VALUES (%s, %s, %s)
            RETURNING message_id;
        """
    exec_commit(create_message, (user_id, user_name, msg_body))

    return {"message": "message created successfully"}

def get_message(message_id):
    """
    grabs message details by message ID
    """
    select_message_sql = """
            SELECT * FROM messages WHERE message_id = %s;
        """
    res = exec_get_one(select_message_sql, (message_id))
    return res if res else []

def delete_message(message_id):
    """
    MODS ONLY: deletes message from table
    """
    delete_message_sql = """
            UPDATE messages
            SET is_deleted = true
            WHERE message_id = %s;
        """
    exec_commit(delete_message_sql, (message_id,))
    return {"message": "message deleted successfully"}

recreate_message_table()