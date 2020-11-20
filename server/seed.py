from .sample_questions import sample_questions
from .model import Question
from .extensions import db

def load_sample_questions():
    """load sample questions into database"""

    for question in sample_questions:
        current_question = question['question']
        incorrect_options = ",".join(question['incorrect'])
        correct_answer = question['correct']

        add_question = Question(question=current_question, option=incorrect_options, answer=correct_answer)

        db.session.add(add_question)
    db.session.commit()
