from flask_restful import Resource, reqparse, request

from db.db_utils import exec_get_one
from db.main.messages import *
from db.main.users import *

class Init(Resource):
    def post(self):
        rebuild_user_tables()
        recreate_message_table()
        return {0: "Success"}, 200

class Version(Resource):
    def get(self):
        return exec_get_one("SELECT VERSION()")