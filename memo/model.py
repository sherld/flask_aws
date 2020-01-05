from datetime import datetime
from memo.database import db


class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column('id', db.Integer, primary_key=True)
    title = db.Column(db.String(60))
    text = db.Column(db.String)
    done = db.Column(db.Boolean)
    pub_date = db.Column(db.DateTime)

    @classmethod
    def readTodos(cls):
        return cls.query.all()

    @classmethod
    def createTodo(cls, title, text):
        return cls(title, text)

    def __init__(self, title, text):
        self.title = title
        self.text = text
        self.done = False
        self.pub_date = datetime.utcnow()

    def create(self):
        db.session.add(self)
        db.session.commit()
        db.session.refresh(self)
