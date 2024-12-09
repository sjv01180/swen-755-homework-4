from flask_restful import Resource, request, reqparse
from db.main.users import _get_user_by_session,get_user,create_user,update_user_session_id,validate_user,invalidate_user,User, _go_back_one_day

BAD_REQUEST_ERROR = {"error": "Bad Request"}
HELP = 'This field cannot be blank'

class Users(Resource):
    """
    implement user actions
    """
    def get(self):
        """
        handle get requests
        """
        parser = reqparse.RequestParser()
        parser.add_argument('session', help=HELP, required=True)
        data = parser.parse_args()

        # Retrieve user by session ID
        cur_user = _get_user_by_session(data['session'])
        if cur_user is None:
            return {"error": "User not found"}, 404

        return {"is_mod": cur_user.is_mod}, 200

    def post(self, action):
        """
        handle user post requests
        """
        if action == 'register':
            return self.register()
        elif action == 'login':
            return self.login()
        elif action == 'logoff':
            return self.logoff()
        elif action == 'goback':
            return self.goback()
        else:
            return BAD_REQUEST_ERROR, 400
        
    def goback(self):
        """
        helper route for reversing last login date for expiration feature
        """
        parser = reqparse.RequestParser()
        parser.add_argument('session', help=HELP, required=True, location='json')
        data = parser.parse_args()
        if not _go_back_one_day(data['session']):
            return {"error": "could not go back in time"}, 401
        return {"success": "time travel successful"}, 200

    def login(self):
        """
        user login function
        """
        parser = reqparse.RequestParser()
        parser.add_argument('username', help=HELP, required=True, location='json')
        parser.add_argument('password', help=HELP, required=True, location='json')

        data = parser.parse_args()

        if not validate_user(data['username'], data['password']):
            return {"error": "username or password is incorrect"}, 401

        session_id = update_user_session_id(data['username'])
        user = get_user(data['username'], session_id)
        # return {"message": "Success"}, 200
        return {"username": user.username, "session": session_id}, 200

    def register(self):
        """
        register user action
        """
        parser = reqparse.RequestParser()
        parser.add_argument('username', help=HELP, required=True)
        parser.add_argument('password', help=HELP, required=True)
        data = parser.parse_args()

        try:
            password = data["password"]
            user = User("uid", data["username"])

            if create_user(user, password):
                return {"username": user.username}, 200
            else:
                return {"error": "username is not unique"}, 401
        except ValueError:
            return {"error": "Invalid parameters"}, 400

    def logoff(self):
        """
        user logoff function
        """
        parser = reqparse.RequestParser()
        parser.add_argument('session', help=HELP, required=True)
        data = parser.parse_args()

        if not invalidate_user(data['session']):
            return {"error": "user could not be logged off"}, 401
        return {"success": "logoff successful"}, 200