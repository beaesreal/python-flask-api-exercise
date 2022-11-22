# add flask
from flask import Flask
app = Flask(__name__)

# add the jsonify method to your Flask import
from flask import Flask, jsonify

# for POST
from flask import request

# function json.loads
import json


# create a global variable todos
todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]


#GET
@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text


# POST
@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data
    print("Incoming request with the following body", request_body)
    decoded_object=json.loads(request_body)
    todos.append(decoded_object)
    return jsonify(todos)


# DELETE
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete: ", position)
    todos.pop(position)
    return jsonify(todos)



#------------>>
# CAUTION!! These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)