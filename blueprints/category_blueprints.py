from flask import Blueprint, jsonify, request
import json


category_bp = Blueprint('category',__name__)


# Load data from JSON file
with open('category.json', 'r') as file:
    categories = json.load(file)

# Helper function to save data to JSON file
def save_data():
    with open('category.json', 'w') as file:
        json.dump(categories, file, indent=4)

# Helper function to find item by ID
def find_category_by_id(category_id):
    for category in categories:
        if category['id'] == category_id:
            return category
    return None

# GET /api/category
@category_bp.route('/category', methods=['GET'])
def get_items():
    return jsonify(categories)

# POST /api/category
@category_bp.route('/category', methods=['POST'])
def create_item():
    data = request.json
    new_category = {
        'id': len(categories) + 1,
        'name': data['name'],
        'isActive': True 
    }
    categories.append(new_category)
    save_data()  # Save data to JSON file
    return jsonify(new_category), 201

# DELETE /api/category/{id}
@category_bp.route('/category/<int:category_id>', methods=['DELETE'])
def delete_item(category_id):
    category = find_category_by_id(category_id)


    if category:
        categories.remove(category)
        save_data()  # Save data to JSON file
        return '', 204
    

    else:
        return jsonify({'error': 'Data not found'}), 404

# PUT /api/category/{id}
@category_bp.route('/category/<int:item_id>', methods=['PUT'])
def update_item(category_id):


    category = find_category_by_id(category_id)


    if category:
        data = request.json
        category['name'] = data['name']
        category['status'] = 'updated'

        save_data()  # Save data to JSON file
        
        return jsonify(category),200
    else:
        return jsonify({'error': 'Data not found'}), 404
