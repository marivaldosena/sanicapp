from sanic.views import HTTPMethodView
from sanic.response import json, text
from app.models import Todo


class TodoListView(HTTPMethodView):
    def get(self, request):
        todos = Todo.find()

        return json({'todos': todos})

    def post(self, request):
        print(request.json)
        todo = Todo(title=request.json.get('title', None),
                    description=request.json.get('description', None))
        todo.save()
        return json(todo)


class TodoView(HTTPMethodView):
    def get(self, request, id):
        return text('GET /api/todos/:id')
