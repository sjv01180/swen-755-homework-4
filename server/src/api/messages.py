from flask_restful import Resource, request, reqparse
from db.main.messages import list_messages, get_message, create_message, delete_message
from db.main.users import get_user

BAD_REQUEST_ERROR = {"error": "Bad Request"}
HELP = 'This field cannot be blank'

class Messages(Resource):
    def get(self):
        return list_messages(), 200
    
    def post(self):
        """
        create new message in messages. Validates user authentication before populating database
        """
        parser = reqparse.RequestParser() # grabs username and session from request body
        parser.add_argument('username', help=HELP, required=True)
        parser.add_argument('session', help=HELP, required=True)
        parser.add_argument('message', help=HELP, required=True)
        data = parser.parse_args()

        # validate user
        cur_user = get_user(data['username'], data['session'])
        if cur_user is None:
            return {"error": "user not authenticated"}, 401
        print(cur_user)
        #write message
        uid = cur_user.uid
        return create_message(uid, data['message']), 200


class SingleMessage(Resource):
    def put(self, message_id):
        """
        change is_deleted flag on individual message
        """
        parser = reqparse.RequestParser() # grabs username and session from request body
        parser.add_argument('username', help=HELP, required=True)
        parser.add_argument('session', help=HELP, required=True)
        data = parser.parse_args()

        # validate mod user
        cur_user = get_user(data['username'], data['session'])
        if cur_user is None:
            return {"error": "user not authenticated"}, 401
        if not cur_user.is_mod:
            return {"error": "user is not a moderator"}, 401
        
        # change message delete flag
        return delete_message(message_id), 200