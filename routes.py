from flask import Blueprint, jsonify, request
import os
import pymongo
from dotenv import load_dotenv
main = Blueprint('main', __name__)

# Connect to MongoDB
dotenv_path = 'C:/Users/gabri/.env'
load_dotenv(dotenv_path)
mongo_password = os.getenv("MONGO_PASSWORD")
mongodb_uri = f"mongodb+srv://thegrimbee:{mongo_password}@cluster0.dcxghro.mongodb.net/"
cluster = pymongo.MongoClient(mongodb_uri)
print('Connected to MongoDB')

# Create database and collection
db = cluster["backend_assignment"]
col = db["assignment_2"]
print('Created database and collection')

@main.route('/', methods=['GET'])
def home():
    try:
        if request.method == "GET":
            return "Hello Backend", 200
    except Exception as e:
        print(f"Error : {e}")
    return "Can't access", 404

            
@main.route('/about_me',methods=['POST'])
def about_me():
    try:
        if request.method == "POST":
            new_data = {
                "Name": "Warren",
                "Course": "Pharaceutical Science",
                "Year": 1, 
                "List all your CCA's": ["Dance", "Takraw", "RHOC", "Phoenix Press"]
            }
            col.insert_one(new_data.copy()) # Used copy since insert_one() modifies the original dictionary, making it unjsonifiable
            print('New Data Added to MongoDB')
            return jsonify(new_data), 201
    except Exception as e:
        print(f"Error : {e}")
    return "Can't add", 404

@main.route('/about_me/<name>', methods=['GET'])
def about_me_with_name(name):
    try:
        if request.method == "GET":
            data = col.find_one({"Name": name})
            if data != None:
                return jsonify(data), 200
            else:
                return "Not Found", 404
    except Exception as e:
        print(f"Error : {e}")
    return "Can't access", 404

@main.route('/add_item', methods=['POST'])
def add_item():
    try:
        if request.method == "POST":
            print('Received POST Request')
            return "Done", 201
    except Exception as e:
        print(f"Error : {e}")
    return "Can't add", 404


