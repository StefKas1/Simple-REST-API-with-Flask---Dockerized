from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

# Adapted from Flask-RESTful.

app = Flask(__name__)
api = Api(app)

# Non-persistent data storage:
# {todo_id: {"task": "description"},
#  todo_id: {"task": "description"}, ...}
# Could be a database.
todos = {
    "todo1": {"task": "do A for task"},
    "todo2": {"task": "do B for task"},
    "todo3": {"task": "do C, D, E for task"},
}


def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in todos:
        abort(404, message="Todo {} does not exist".format(todo_id))


parser = reqparse.RequestParser()
parser.add_argument("task")

# GET 	 /todos : Gets all todos, and thus all tasks.
# POST 	 /todos : Creates a new todo (if same POST is done, new todo is created every time).

# GET 	 /todos/{todo_id} : Gets one todo with key todo_id.
# PUT 	 /todos/{todo_id} : Updates one todo with key todo_id.
# (^^ if todo_id does not exist, first PUT creates entry; second PUT updates entry).
# DELETE /todos/{todo_id} : Deletes one todo with key todo_id.


class TodoList(Resource):
    def get(self):
        a = 3
        """Returns JSON/dict of all todos.
        """
        return todos

    def post(self):
        """Adds one todo to JSON/dict, and returns added todo and status code 201.
        """
        args = parser.parse_args()
        todo_id = "todo%d" % (len(todos) + 1)
        todos[todo_id] = {"task": args["task"]}
        return todos[todo_id], 201


class Todo(Resource):
    def get(self, todo_id):
        """Returns JSON/dict of one todo with key todo_id.
        """
        abort_if_todo_doesnt_exist(todo_id)
        return todos[todo_id]

    def put(self, todo_id):
        """If todo_id does not exist, adds entry - else updates entry with key todo_id.
        And returns added/updated todo and status code 201.
        """
        args = parser.parse_args()
        task = {"task": args["task"]}
        todos[todo_id] = task
        return task, 201

    def delete(self, todo_id):
        """Deletes JSON/dict item of one todo with key todo_id.
        And returns empty string and status code 204.
        """
        abort_if_todo_doesnt_exist(todo_id)
        del todos[todo_id]
        return "", 204


# Adds resource(s) to the REST api.
# Note, parameter 'todo_id' of methods of Todo class must match with part after "/todos/<string:"
api.add_resource(TodoList, "/todos")
api.add_resource(Todo, "/todos/<string:todo_id>")


if __name__ == "__main__":
    app.run(debug=True,
            host="0.0.0.0")  # host=... to allow server access via network.
