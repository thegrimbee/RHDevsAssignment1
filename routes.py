from flask import Blueprint, jsonify, request
main = Blueprint('main', __name__)

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
            return jsonify({
                "Name": "Gabriel",
                "Course": "Computer Science",
                "Year": 1, 
                "List all your CCA's": ["RHDevs", "COMMotion", "Takraw", "Tech Crew", "EML"]
            }), 201
    except Exception as e:
        print(f"Error : {e}")
    return "Can't add", 404


@main.route('/add_item', methods=['POST'])
def add_item():
    try:
        if request.method == "POST":
            print('Received POST Request')
            return "Done", 201
    except Exception as e:
        print(f"Error : {e}")
    return "Can't add", 404


