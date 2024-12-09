# swen-755-homework-5
This is the main repository for assignment 5 on arch breakers.

Four Architecture Breakers in Session Management Architecture:
1. SESSION EXPIRATION MANAGEMENT: Allows for session hijacking due to indefinite use time within the session. Users who have left their session open and have their session hijacked can have malicious actions falsely attributed to them. One solution would be to include session expiration after time since session open, or based on inactivity
    - Most of out tests focus on this breaker, as there was no session expiration mechanism established prior to this assignment.

2. ROLE VERIFICATION: Users may have more or less permissions than intended. Users lacking their intended permissions may be unable to perform critical tasks, and users with more than intended permissions may be able to access private data. Solutions include implementing multiple Role Based Access Control policies within the system, Auditing and logging of system actions, and Rigorous role-based testing prior to deployment.
    - Role Verification was already implemented on our code, so no tests were written for this breaker.

3. SESSION TOKEN STORAGE SECURITY: Session Token storage may be easy to access, allowing for session tokens to be accessed by non-admin actors. Actions may be taken by malicious actors under the guise of another user, invalidating audits and logs. Solutions include Using role-based access to session tokens, Ensuring access of session tokens is done through encrypted channels, and Ensuring storage of tokens is encrypted.
    - Session tokens are pre-encrypted through salts prior to generation. Thus, no tests were written for this breaker.

4. SESSION TOKEN GENERATION WEAKNESS: Session tokens may be easy to predict, therefore making session easy to hijack or spoof. Users may have their sessions hijacked due to being predicted, allowing malicious actors to perform actions as another user. Solutions include Using complex token generation, and Auditing and logging session activation and access.
    - Session token generation is done using a SHA-256 encryption algorithm, making it difficult to predict. Thus, no tests were written for this breaker.

HOW TO RUN PROGRAM:
Before running the project, we need to install some important python libraries in our environment. Type the following code onto the terminal and press enter. pip install -r ./server/requirements.txt .
To run the server, go to the server directory and run the following command: python src/server.py. Theoretically, you should be able to run the python script with no issues. Otherwise, you might need to install and configure postgres in your local machine. 
Once the server is running, open /frontend/public/messageboard.html in your system’s file directory. Be sure to open the browser console to see important console messages. Ideally, the site should redirect you to the login page, but you might see a message board and a form to enter a new message. If you try to submit a message, you will receive an error message stating that you were unauthenticated.
Now go to /frontend/public/index.html to access the web application. You will see a simple interface for logging into an account. If you submit a random username and password, the site will give you an auth error. Fortunately, we have seeded the backend with user accounts and messages. Proceed to log in with the following credentials:
Username: JaneFonda
Password: 123
You will be redirected to the messageboard page as user JaneFonda. If you look into the browser console, you will see a logged message containing the session token. This will be useful for later. For now, type a message onto the textbox and click “post message”. As an authenticated user, the browser should accept your input and update the message board with your new message.
If you attempt to doubleclick on the “Delete” button for any of the messages, the browser will print the uuid value of the corresponding message record and give you an error. This is because CORS is the scourge of the earth and fickle for fullstack development. Keep note of the uuid value, as this will be important for later.
On your machine, open Postman or any other API development tool. Enter a new PUT request with the following url: http://localhost:8080/messages/<message_id>. Here, you can replace the message id with the one generated in the browser console from step 6. Access the request body editor on the tool and set the request body format to raw JSON. Before sending, your request should look like the following image below. For the “session” parameter value, copy the value generated in the browser console from step 5 and paste it as a string.

The response output from the API development tool should generate a simple json result, stating that the message was deleted successfully. Since JaneFonda is a moderator account, it has permission to delete messages from the message board. Go back to the web browser containing our message board ui and refresh the page. Once loaded, the contents of the message clicked from step 6 will be replaced with “Message Deleted”.


