from flask import Flask
from pymongo import MongoClient
import os

app = Flask(__name__)

# Подключение к MongoDB через переменную среды
mongo_uri = os.environ.get("MONGO_URI", "mongodb://localhost:27017/mydb")
client = MongoClient(mongo_uri)
db = client.get_database()

@app.route('/')
def home():
    return 'Hello, Docker & MongoDB!!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
