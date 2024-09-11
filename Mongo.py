import redis
import json
from pymongo import MongoClient
from flask import Flask, jsonify

app = Flask(__name__)
redis_client = redis.StrictRedis(host='10.1.0.158', port=6379, decode_responses=True)
mongo_client = MongoClient('mongodb+srv://admin:admin@redis.7zqfwsd.mongodb.net/?appName=mongosh+2.2.5')
db = mongo_client['redis-user']
collection = db['Users']

@app.route('/data')
def get_data():
    key = 'cached_data'
    cached_data = redis_client.get(key)
    #cached_data = 0
    if cached_data:
        return jsonify(cached_data)
    else:
        #data = list(collection.find())
        data = list(collection.find({},{'_id':0, 'name':1, 'age':1}))
        if data:
               redis_client.set(key, json.dumps(data), ex=3600)
               return jsonify(data)
        else:
               return 'Data not found', 404

if __name__ == '__main__':
    app.run(debug=True, host='192.168.64.1')