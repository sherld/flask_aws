from flask import request
from flask_restful import Resource
from .model import Todo


class MemoList(Resource):

    def convertToDto(self, todo):
        return {'id': todo.id, 'text': todo.text,
                'title': todo.title, 'done': todo.done}

    def get(self):
        todos = Todo.readTodos()
        ret = list(map(lambda todo: self.convertToDto(todo), todos))
        return list(ret)

    def post(self):
        requestBody = request.get_json()
        todo = Todo.createTodo(requestBody['title'], requestBody['text'])
        todo.create()
        return self.convertToDto(todo)