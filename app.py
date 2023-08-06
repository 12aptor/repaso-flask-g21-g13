from flask import Flask
from flask_cors import CORS
from users import users_list

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Bienvenido a mi API! 😎'

@app.route('/users')
def users():
    return users_list

if __name__ == '__main__':
    app.run(debug=True)