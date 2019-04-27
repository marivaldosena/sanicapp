from sanic import Sanic
from sanic.response import json


app = Sanic(__name__)


@app.route('/')
async def main(request):
    return json({'hello': 'world'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, workers=2)