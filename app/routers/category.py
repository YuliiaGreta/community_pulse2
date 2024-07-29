from flask import Blueprint, request, jsonify
from app.models import db, Category
from app.schemas.category import CategoryCreate, CategoryResponse
from pydantic import ValidationError

category_bp = Blueprint('category', __name__)

@category_bp.route('/categories', methods=['GET'])
def get_categories():
    categories = Category.query.all()
    return jsonify([CategoryResponse.from_orm(c) for c in categories])

@category_bp.route('/categories', methods=['POST'])
def add_category():
    data = request.get_json()
    try:
        category_data = CategoryCreate(**data)
    except ValidationError as e:
        return jsonify(e.errors()), 400

    new_category = Category(name=category_data.name)
    db.session.add(new_category)
    db.session.commit()
    return jsonify(CategoryResponse.from_orm(new_category)), 201

@category_bp.route('/categories/<int:id>', methods=['PUT'])
def update_category(id):
    data = request.get_json()
    category = Category.query.get_or_404(id)
    try:
        category_data = CategoryCreate(**data)
    except ValidationError as e:
        return jsonify(e.errors()), 400

    category.name = category_data.name
    db.session.commit()
    return jsonify(CategoryResponse.from_orm(category))

@category_bp.route('/categories/<int:id>', methods=['DELETE'])
def delete_category(id):
    category = Category.query.get_or_404(id)
    db.session.delete(category)
    db.session.commit()
    return '', 204