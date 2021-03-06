from flask import Blueprint, jsonify, request 
from flask_cors import CORS
import sys
import random

from .model import Question, Message
from .extensions import db
from .helpers import shuffleOptions

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
    options = ("/").join(new_question["options"])
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

@api.route('/api/getQuestion', methods=["POST", "GET"])
def get_question():
    """given a number, return the number of questions equals to the number"""

    questions_number = request.get_json()
    
    if not questions_number:
        return jsonify("Unable to get questions, please try again."), 400


    try:
        all_query = Question.query.all()
        questions_ids = set()
        questions = []
        while len(questions_ids) != questions_number:
            chosen_question = random.choice(all_query)
            print(chosen_question.id)
            if chosen_question.id not in questions_ids:
                questions_ids.add(chosen_question.id)
                options = shuffleOptions(chosen_question.option, chosen_question.answer)
                
                question = {
                    "question": chosen_question.question,
                    "options": options,
                    "answer": chosen_question.answer
                }
                questions.append(question)
        
        return jsonify(questions), 200
    except: 
        return jsonify("Unable to get questions, please try again."), 400

@api.route('/api/addMessage', methods=["POST", "GET"])
def post_message():
    """given a message, add message to the database"""

    message_response = request.get_json()


    try:
        name = message_response["name"]
        message = message_response["message"]
        new_message = Message(message=message, name=name)
        db.session.add(new_message)
        db.session.commit()
        return jsonify("Message added"), 200
    except:
        return jsonify("There was an issue adding the message, please try again."), 400
    
@api.route('/api/getMessage', methods=["POST", "GET"])
def get_message():
    """get back birthday messages from the backend"""

    try:
        all_messages = Message.query.all()
        messages = []

        for message in all_messages:
            single_message = {
                "message": message.message,
                "name": message.name
            }
            messages.append(single_message)
        
        return jsonify(messages), 200
    except:
        return jsonify("Unable to retrieve messages, please try again")












    
        
