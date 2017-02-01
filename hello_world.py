from flask import Flask
from os import environ

app = Flask(__name__)

@app.route("/")
@app.route("/hello")
def say_hi():
        return "Hello World!"
    
@app.route("/hello/<name>")
def hello_person(name):
    html = """
    <h1>
            Hello {}!
        <h1>
        <p>
            Here's a picture of a kitten. Awww...
        </p>
        <img src="http://placekitten.com.s3.amazonaws.com/homepage-samples/408/287.jpg">
    """
    return html.format(name.title())
    
@app.route("/hello/jedi/<first_name>/<last_name>")
def jedi_person(first_name, last_name):
    first_name = first_name[0:2]
    last_name = last_name[0:3]
    html = """
    <h1>
        What is your Jedi name?
    </h1>
    <p> 
        Your jedi name is "{}{}"
    </p>
    <img src="https://images.unsplash.com/profile-fb-1465355193-c3fa695c1fda.jpg?ixlib=rb-0.3.5&q=80&fm=jpg&crop=faces&cs=tinysrgb&fit=crop&h=128&w=128&s=48c018887476054afc6edccbc5e5fa30">
    """
    return html.format(last_name, first_name)
    
        
if __name__ == "__main__":
    app.run(host=environ['IP'],
        port=int(environ['PORT']))

        