from flask import Blueprint, request, jsonify
from app.models import db, Response

response_bp = Blueprint('response', __name__)

@response_bp.route('/responses', methods=['GET'])
def get_responses():
    responses = Response.query.all()
    return jsonify([{'id': r.id, 'question_id': r.question_id, 'agree': r.agree, 'count': r.count} for r in responses])

@response_bp.route('/responses', methods=['POST'])
def add_response():
    data = request.get_json()
    new_response = Response(question_id=data['question_id'], agree=data['agree'], count=data['count'])
    db.session.add(new_response)
    db.session.commit()
    return jsonify({'id': new_response.id, 'question_id': new_response.question_id, 'agree': new_response.agree, 'count': new_response.count}), 201