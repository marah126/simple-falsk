
from flask import Flask, render_template, request
from markupsafe import escape

app = Flask(__name__)

# first simple API just to print Hello World!
@app.route('/')
def hello_world():  # put application's code here
    return '<h1>Hello World! </h1>'

# This API take the name from the URL
@app.route("/name/<name>")
def hello(name):
    return "Hello, {}!".format(name)

# This API to return html page
@app.route("/ttt")
def show_template():
    return render_template("index.html")

# This API to set the allowed methods
@app.route('/method', methods=['POST', 'GET', 'PUT', 'DELETE'])
def show_method():
    if request.method == "GET":
        return "<h1> The method used is GET</h1>"
    elif request.method == "POST":
        return "<h1> The method used is POST</h1>"
    elif request.method == "PUT":
        return "<h1> The method used is PUT</h1>"
    elif request.method == "DELETE":
        return "<h1> The method is DELETE</h1>"

# This API to use post function and send the data in body of request in json format
@app.post("/post")
def use_post():
    data=request.json
    first_name = data['first_name']
    last_name = data.get('last_name')

    return first_name + " " + last_name


if __name__ == '__main__':
    app.run(debug=True)
