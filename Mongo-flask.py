from flask import Flask,request
from flask_pymongo import PyMongo
from flask_restplus import Api, Resource, fields
from flask_cors import CORS


app = Flask(__name__)
CORS(app)



app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"


api = Api(app,
          version="1.0",
          title="BML Interns",
          description="BML Interns")
api = api.namespace('', 'BML')

mongo = PyMongo(app)

m_user = api.model('user', {'username': fields.String('user'), 'password': fields.String('password')})

@app.after_request
def allow_cross_domain(response):
    """Hook to set up response headers."""
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'content-type'
    response.headers.add("Access-Control-Allow-Methods", "GET, POST, OPTIONS, PUT, DELETE");
    return response

@app.route('/')
def hello_world():
    return 'Hello World!'


@api.route('/user')
class User(Resource):
    def get(self):
        user_collection = mongo.db.bmlusers
        user = user_collection.find()
        m_user1 = []
        for result in user:
            print(result)
            m_user1.append(result['username'])

        return m_user1

    @api.expect(m_user)
    def put(self):
        data = request.get_json()
        user_collection = mongo.db.bmlusers
        user = user_collection.find_one({'username': data['username']})
        password = data['password'].encode('utf-8')
        if user:
            user['password'] = password
            user_collection.save(user)
            return {'message': 'User Modified'}
        else:
            user_collection.insert(
                {'username': data['username'], 'role': 'user', 'password': password})

            return {'message': 'User Has been Added'}

    @api.expect(m_user)
    def delete(self):
        data = request.get_json()
        user_collection = mongo.db.bmlusers
        user = user_collection.find_one({'username': data['username']})
        password = data['password'].encode('utf-8')
        if user:

            user_collection.remove(user)
            return {'message': 'User Deleted'}
        else:

            return {'message': 'User Not exists'}


    @api.expect(m_user)
    def post(self):
        data = request.get_json()
        user_collection = mongo.db.bmlusers
        user = user_collection.find_one({'username': data['username']})
        password = data['password'].encode('utf-8')
        if user:
            return {'message': 'User Already Exists'}
        else:
            user_collection.insert(
                {'username': data['username'], 'role': 'user', 'password': password})

            return {'message': 'User Has been Added'}
@app.after_request
def allow_cross_domain(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'content-type'
    response.headers.add("Access-Control-Allow-Methods", "GET, POST, OPTIONS, PUT, DELETE");
    return response

if __name__ == "__main__":
    app.run(host='localhost', port=5000)

