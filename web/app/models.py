import json
from pymongo import MongoClient, collection

mongo = MongoClient('mongodb://localhost:27017')
db = mongo.sanicapp


class Todo():
    def __init__(self, title, description):
        self.title = title
        self.description = description

    def to_json(self):
        todo = {
            'id': str(self.id),
            'title': self.title,
            'description': self.description
        }

        return todo

    @classmethod
    def find(cls):
        result = db.todos.find()  

        todos = [Todo.find_one(item.get('_id')) for item in result]
        return todos

    def save(self):
        result = db.todos.insert_one({
            'title': self.title,
            'description': self.description
        })
        self.id = '{}'.format(result.inserted_id)

    @classmethod
    def find_one(cls, *args, **kwargs):
        query = None

        if kwargs.get('id'):
            query = {'_id': collection.ObjectId(kwargs.get('id', None))}
        elif kwargs.get('title'):
            query = {'title': kwargs.get('title')}
        elif kwargs.get('description'):
            query = {'description': kwargs.get('description')}

        result = db.todos.find_one(query)
        todo = cls(result.get('title'), result.get('description'))
        todo.id = str(result.get('_id'))
        return todo

    def delete(self):
        if self.id:
            db.todos.delete_one({'id': collection.ObjectId(self.id)})
            return self
