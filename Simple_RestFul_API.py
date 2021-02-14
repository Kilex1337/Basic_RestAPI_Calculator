from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

def checkPostedData(postedData):
    if "x" not in postedData or "y" not in postedData:
        return 301
    else:
        return 200

class Add(Resource):
    def post(self):
        # If i am here, then the resource Add was requested using the method POST
        # Step 1: Get posted data
        postedData = request.get_json()

        # Step 1b: Verify Validity of posted data
        status_code = checkPostedData(postedData)
        if status_code != 200:
            retJson = {
                "Message": "An error happened",
                "Status Code": status_code
            }
            return jsonify(retJson)

        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)

        # Step 2: Add the posted data
        ret = x + y
        retMap = {
            "Message": ret,
            "Status Code": 200
        }

        # Step 3: Return the response to the user
        return jsonify(retMap)

class Subtract(Resource):
    def post(self):
        postedData = request.get_json()

        status_code = checkPostedData(postedData)
        if status_code != 200:
            retJson = {
                "Message": "An error happened",
                "Status Code": status_code
            }
            return jsonify(retJson)

        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)
        ret = x - y
        retMap = {
            "Message": ret,
            "Status Code": 200
        }
        return jsonify(retMap)

class Divide(Resource):
    def post(self):
        postedData = request.get_json()

        status_code = checkPostedData(postedData)
        if status_code != 200:
            retJson = {
                "Message": "An error happened",
                "Status Code": status_code
            }
            return jsonify(retJson)

        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)
        try:
            ret = x / y
            retMap = {
                "Message": ret,
                "Status Code": 200
            }
            return jsonify(retMap)
        except ZeroDivisionError:
            ret = "Can't divide by 0 ('y' is zero)"
            retMap = {
                "Message": ret,
                "Status code": 302
            }
            return jsonify(retMap)

class Multiply(Resource):
    def post(self):
        postedData = request.get_json()

        status_code = checkPostedData(postedData)
        if status_code != 200:
            retJson = {
                "Message": "An error happened",
                "Status Code": status_code
            }
            return jsonify(retJson)

        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)
        ret = x * y
        retMap = {
            "Message": ret,
            "Status Code": 200
        }
        return jsonify(retMap)

# This is mandatory for the api to work
api.add_resource(Add, "/add")   # First the resource then the path
api.add_resource(Subtract, "/subtract")
api.add_resource(Multiply, "/multiply")
api.add_resource(Divide, "/divide")

@app.route('/')
def hello_world():
    return "Hello World!"


if __name__ == "__main__":
    app.run(debug = True)
