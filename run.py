from flask import Flask, request, jsonify
from itertools import islice

app = Flask(__name__)

# get
@app.route('/id/<int:id>', methods = ['GET']) 
def get(id):
    if id >= 5000:
        resource = {'result' : True}
    else:
        resource = {'result' : False}
    return resource

# post  
@app.route('/id', methods = ['POST'])
def post():
    user = request.get_json()
    '''
    user = {
        "name" : "kim",
        "value" : 1357
    }
    '''
    return "{ name : " + user["name"] + " }"
    
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)