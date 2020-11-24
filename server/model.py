from .extensions import db

class Question(db.Model):
    __tablename__ = "questions"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    question = db.Column(db.String, nullable=False)
    option = db.Column(db.String, nullable=False)
    answer = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"<question={self.question}>"

class Message(db.Model):
    __tablename__ = "messages"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    message = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"<message={self.message}>"
    
