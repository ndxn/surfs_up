from flask import Flask
app = Flask(__name__)

# Define the root
@app.route('/')
def helloWorld():
    return "Hello World"

helloWorld
