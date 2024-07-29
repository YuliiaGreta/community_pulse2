from flask import Blueprint, request, jsonify
from app.models import db, Question, Category
from app.schemas.question import QuestionCreate, QuestionResponse
from pydantic import ValidationError

questions_bp = Blueprint('questions', __name__)

@questions_bp.route('/questions', methods=['GET'])
def get_questions():
    questions = Question.query.all()
    return jsonify([QuestionResponse.from_orm(q) for q in questions])

@questions_bp.route('/questions', methods=['POST'])
def add_question():
    data = request.get_json()
    try:
        question_data = QuestionCreate(**data)
    except ValidationError as e:
        return jsonify(e.errors()), 400

    new_question = Question(text=question_data.text, category_id=question_data.category_id)
    db.session.add(new_question)
    db.session.commit()
    return jsonify(QuestionResponse.from_orm(new_question)), 201