from sanic import Sanic
from sanic.response import json
from app.routes import TodoView

app = Sanic(__name__)

@app.route('/')
async def main(request):
    return json({'hello': 'world'})

app.add_route(TodoView.as_view(), '/api/todos')
