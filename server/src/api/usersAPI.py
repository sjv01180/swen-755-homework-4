from flask_restful import Resource, request, reqparse
from db.main.users import clear_users,get_user,create_user,update_user_session_id,validate_user,invalidate_user,User

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
        pass

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
        else:
            return BAD_REQUEST_ERROR, 400

    def login(self):
        """
        user login function
        """
        parser = reqparse.RequestParser()
        parser.add_argument('username', help=HELP, required=True)
        parser.add_argument('password', help=HELP, required=True)

        data = parser.parse_args()

        if not validate_user(data['username'], data['password']):
            return {"error": "username or password is incorrect"}, 401

        session_id = update_user_session_id(data['username'])
        user = get_user(data['username'], session_id)
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