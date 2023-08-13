from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Text, Boolean

app = Flask(__name__)
db = SQLAlchemy()
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:root@localhost:3306/flask_repaso"

db.init_app(app)

class UserModel(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    password = Column(Text, nullable=False)
    status = Column(Boolean, default=True)

@app.route('/')
def hello_world():
    return 'Hello, World! 😎'

if __name__ == '__main__':
    app.run(debug=True)