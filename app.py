# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

items = []

@app.route('/item', methods=['POST'])
def create_item():
    data = request.get_json()
    item = {"name": data["name"], "price": data["price"]}
    items.append(item)
    return jsonify(item), 201

@app.route('/item/<string:name>', methods=['GET'])
def get_item(name):
    for item in items:
        if item["name"] == name:
            return jsonify(item)
    return {"message": "Item not found"}, 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)
 
