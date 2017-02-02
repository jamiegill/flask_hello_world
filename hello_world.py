from flask import Flask, render_template
from os import environ

app = Flask(__name__)

@app.route("/")
@app.route("/hello")
def say_hi():
        return "Hello World!"
    
@app.route("/hello/<name>")
def hello_person(name):
    return render_template('hello_template.html',
                            name=name)
    
@app.route("/hello/jedi/<first_name>/<last_name>")
def jedi_person(first_name, last_name):
    first_name = first_name[0:2]
    last_name = last_name[0:3]
    return render_template('jedi_template.html',
                            last_name=last_name,
                            first_name=first_name)
    
        
if __name__ == "__main__":
    app.run(host=environ['IP'],
        port=int(environ['PORT']))

        