from sanic.views import HTTPMethodView
from sanic.response import json, text
from app.models import Todo


class TodoListView(HTTPMethodView):
    def get(self, request):
        todos = Todo.find()

        return json({'todos': todos})

    def post(self, request):
        todo = Todo(title=request.json.get('title', None),
                    description=request.json.get('description', None))
        todo.save()
        return json(todo)


class TodoView(HTTPMethodView):
    def get(self, request, id):
        todo = Todo.find_one(id=id)

        return json(todo)
