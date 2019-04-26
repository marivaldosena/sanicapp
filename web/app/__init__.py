from sanic import Sanic
from sanic.response import json


app = Sanic(__name__)

@app.route('/')
async def main(request):
    return json({'hello': 'world'})
