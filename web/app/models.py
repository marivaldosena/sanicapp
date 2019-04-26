from pymongo import MongoClient, collection

mongo = MongoClient('mongodb://localhost:27017')
db = mongo.sanicapp


class Todo():
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def save(self):
        result = db.todos.insert_one({
            'name': self.name,
            'description': self.description
        })
        self.id = result.inserted_id


    @classmethod
    def find_one(cls, id):
        result = db.todos.find_one({'_id': collection.ObjectId(id)})
        todo = Todo(result.name, result.description)
        todo.id = result.id
        return todo

