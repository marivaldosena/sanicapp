from pymongo import MongoClient, collection

mongo = MongoClient('mongodb://localhost:27017')
db = mongo.sanicapp


class Todo():
    def __init__(self, title, description):
        self.title = title
        self.description = description

    def save(self):
        result = db.todos.insert_one({
            'title': self.title,
            'description': self.description
        })
        self.id = result.inserted_id

    @classmethod
    def find_one(cls, *args, **kwargs):
        if kwargs.get('id'):
            result = db.todos.find_one(
                {'_id': collection.ObjectId(kwargs.get('id', None))})
        elif kwargs.get('title'):
            result = db.todos.find_one({'title': kwargs.get('title')})
        elif kwargs.get('description'):
            result = db.todos.find_one(
                {'description': kwargs.get('description')})

        todo = cls(result.get('title'), result.get('description'))
        todo.id = str(result.get('_id'))
        return todo

    def delete(self):
        if self.id:
            db.todos.delete_one({'id': collection.ObjectId(self.id)})
            return self