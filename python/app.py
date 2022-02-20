from flask import Flask
from lambda_function import *
app = Flask(__name__)

@app.route('/')
def hello_world():
    return lambda_handler("","")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
