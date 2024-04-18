from flask import Blueprint, jsonify, request
import json

items_bp = Blueprint('items', __name__)

# Load data from JSON file
with open('data.json', 'r') as file:
    items = json.load(file)

# Helper function to save data to JSON file
def save_data():
    with open('data.json', 'w') as file:
        json.dump(items, file, indent=4)

# Helper function to find item by ID
def find_item_by_id(item_id):
    for item in items:
        if item['id'] == item_id:
            return item
    return None

# GET /api/items
@items_bp.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

# POST /api/items
@items_bp.route('/items', methods=['POST'])
def create_item():
    data = request.json
    new_item = {
        'id': len(items) + 1,
        'name': data['name']
    }
    items.append(new_item)
    save_data()  # Save data to JSON file
    return jsonify(new_item), 201

# DELETE /api/items/{id}
@items_bp.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    item = find_item_by_id(item_id)
    if item:
        items.remove(item)
        save_data()  # Save data to JSON file
        return '', 204
    else:
        return jsonify({'error': 'Item not found'}), 404

# PUT /api/items/{id}
@items_bp.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = find_item_by_id(item_id)
    if item:
        data = request.json
        item['name'] = data['name']
        save_data()  # Save data to JSON file
        return jsonify(item), 200
    else:
        return jsonify({'error': 'Item not found'}), 404
