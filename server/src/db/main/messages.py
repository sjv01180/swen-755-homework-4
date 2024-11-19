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
        FROM Messages
    """