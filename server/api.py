from flask import Blueprint, jsonify, request 
from flask_cors import CORS
import sys

from .model import Question
from .extensions import db

api = Blueprint("api", __name__)

CORS(api)

@api.route('/api/hello')
def say_hello():
    return jsonify("hello")

@api.route('/api/addQuestion', methods=["POST", "GET"])
def add_question():
    """add new question to database"""

    new_question = request.get_json()
    question = new_question["question"]
    options = (",").join(new_question["options"])
    answer = new_question["answer"]

    if not question or not options or not answer: 
        return jsonify("There was an issue adding a question, please provide a valid question with options and an answer"), 400
    

    try:
        new_question = Question(question=question, option=options, answer=answer)
        db.session.add(new_question)
        db.session.commit()
        return jsonify('Thank you! You question has been added.'), 200
    except: 
        print("Unexpected error:", sys.exc_info()[0])
        return jsonify("There was an issue adding a question, please try again.")