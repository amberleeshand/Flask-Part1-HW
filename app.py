import os

from flask import Flask, Response, request, app, url_for
app = Flask(__name__)

@app.route('/get/text/')
def get_text():
    return Response("Hello from Flask and TEAM A using an explicit Response object", mimetype='text/plain')

# @app.route('/get/text/about')
# def get_about():
#     return Response("We are testing an about section!!!! TBC", mimetype='text/plain')

@app.route('/get/text/about')
def get_about():
    return f"""
<html>
<head>
    <title>About</title>
</head>
<body>
    <h1>About</h1>
    <p>You have so much to share, would love to learn more about you</p>
    <hr>
    <br>
    <p>Please update this page so we can learn more!</p>
</body>
</html>
"""

@app.route("/index/<name>/<int:age>")
def index(name, age):
    url = url_for('get_text')
    url_about = url_for('get_about')
    return f"""
<html>
<head>
    <title>Sample - A Team Flask routes</title>
</head>
<body>
    <h1>{name} page</h1>
    <p>Hello, {name}</p>
    <p>You are {age} year(s) old.</p>
    <hr>
    <a href="{url}">Welcome</a>
    <a href="{url_about}">About</a>
</body>
</html>
"""

if __name__=="__main__":
    app.run(host=os.getenv('IP', '0.0.0.0'),
            port=int(os.getenv('PORT', 4444)))
