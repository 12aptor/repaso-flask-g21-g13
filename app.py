from flask import Flask, request
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

    def toJson(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'status': self.status
        }

@app.route('/')
def hello_world():
    return 'Hello, World! 😎'

@app.route('/users', methods=['GET'])
def get_users():
    record = UserModel.query.all()
    response = []
    for user in record:
        response.append(user.toJson())
    return response

@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    record = UserModel.query.filter_by(id=id).first()
    response = record.toJson()
    return response

@app.route('/users', methods=['POST'])
def create_user():
    try:
        json = request.get_json()
        user = UserModel(name=json['name'],email=json['email'], password=['password'])
        db.session.add(user)
        db.session.commit()

        response = user.toJson()
        return response, 201
    except Exception as error:
        return {'message': 'Error'}, 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)