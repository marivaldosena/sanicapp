from sanic.views import HTTPMethodView
from sanic.response import json, text
from app.models import Todo


class TodoView(HTTPMethodView):
    def get(self, request):
        return text('GET /api/todos')
