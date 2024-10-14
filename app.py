from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data to mimic database entries
items = [
    {"id": 1, "name": "Item1", "price": 10.0},
    {"id": 2, "name": "Item2", "price": 15.0},
    {"id": 3, "name": "Item3", "price": 8.0}
]

# 1. GET /items - Fetch all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items), 200

# 2. GET /items/<id> - Fetch a single item by ID
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item:
        return jsonify(item), 200
    return jsonify({"error": "Item not found"}), 404

# 3. POST /items - Add a new item
@app.route('/items', methods=['POST'])
def add_item():
    new_item = request.get_json()
    new_item["id"] = len(items) + 1
    items.append(new_item)
    return jsonify(new_item), 201

# 4. PUT /items/<id> - Update an item by ID
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item:
        data = request.get_json()
        item.update(data)
        return jsonify(item), 200
    return jsonify({"error": "Item not found"}), 404

# 5. DELETE /items/<id> - Delete an item by ID
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item["id"] != item_id]
    return jsonify({"message": "Item deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)
