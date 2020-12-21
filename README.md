task #1
the cass from the first task is stored in magic_list.py

task #2
the endpoint needed to retrieve a token is /auth. the username is 'evyatar' and password is 'pass'
to retrieve one you need to send a post request to this endpoint and the body should be:
{
    "username": "evyatar",
    "password": "pass"
}

the response will be a json object with 'token' as the key for the token it self

the second endpoint to normalize the data is /norm
to run the server, run the sanic_server.py module

task #3
the endpoint is as in task #2 (/norm)




