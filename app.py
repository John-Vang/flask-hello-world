# ---- Flask Hello World ---- #

# import the Flask class from the flask package
from flask import Flask

# create the application object
app = Flask(__name__)

# use the decorator pattern to
# link the view fucntion to a url

# static route
@app.route("/")
@app.route("/hello")
# define the view using a function, which returns a string
def hello_world():
    return "Hello, world!"
# dynamic route
# # Repsonse Object, <search_query>, which take the query parameter as an argument that simply returns it
@app.route("/test/<search_query>")
def search(search_query):
    return search_query
# integer route
@app.route("/integer/<int:value>")
def int_type(value):
    print(value + 1)
    return "correct"

# float route
@app.route("/float/<float:value>")
def float_type(value):
    print(value + 1)
    return "correct"

# dynamic route that accepts slashes
@app.route("/path/<path:value>")
def path_type(value):
    print(value)
    return "correct"
# Reponse Object
@app.route("/name/<name>")
def index(name):
    if name.lower() == "michael":
        return f"Hello, {name}", 200"
    else:
        return "Not Found", 404


# start the development server using the run() method
if __name__ == "__main__":
    app.run()
