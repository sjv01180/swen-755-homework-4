from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from api.management import Version, Init
from api.usersAPI import Users
from api.messages import Messages, SingleMessage

app = Flask(__name__)
CORS(app)
api = Api(app)


# Management APIs
api.add_resource(Init, "/manage/init")
api.add_resource(Version, "/manage/version")

# # User APIs
api.add_resource(Users, '/users/<string:action>', endpoint='User_action')
api.add_resource(Users, '/users/role', endpoint='user_role')

# Message APIs
api.add_resource(Messages, '/messages')
api.add_resource(SingleMessage, '/messages/<string:message_id>')


if __name__ == "__main__":
    app.run(debug=True, port=8080)