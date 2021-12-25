from requests import get, post, put, delete

BASE_URL = "http://localhost:5000"

##########################
# Requests to /todos
##########################
print("--- GET /todos ---")
# GET 	 /todos : Gets all todos, and thus all tasks.
response = get(f"{BASE_URL}/todos")
print(response.json())

print("\n--- POST /todos ---")
# POST 	 /todos : Creates a new todo (if same POST is done, new todo is created every time).
response = post(f"{BASE_URL}/todos", data={"task": "do F for task"})
response = post(f"{BASE_URL}/todos", data={"task": "do F for task"})
print(response.json())
# GET 	 /todos : Gets all todos, and thus all tasks.
response = get(f"{BASE_URL}/todos")
print(response.json())


##########################
# Requests to /todos/{todo_id}
##########################
# GET 	 /todos/{todo_id} : Gets one todo with key todo_id.
print("\n--- GET /todos/{todo_id} ---")
response = get(f"{BASE_URL}/todos/todo1")
print(response.json())

# PUT 	 /todos/{todo_id} : Updates one todo with key todo_id
# (^^ if todo_id does not exist, first PUT creates entry; second PUT updates entry).
print("\n--- PUT /todos/{todo_id} ---")
response = put(f"{BASE_URL}/todos/todo2",
               data={"task": "task was updated"})
print(response.json())
# GET 	 /todos : Gets all todos, and thus all tasks.
response = get(f"{BASE_URL}/todos")
print(response.json())

# DELETE /todos/{todo_id} : Deletes one todo with key todo_id.
print("\n--- DELETE /todos/{todo_id} ---")
response = delete(f"{BASE_URL}/todos/todo1")
assert response.status_code == 204
print(response.status_code)
# GET 	 /todos : Gets all todos, and thus all tasks.
response = get(f"{BASE_URL}/todos")
print(response.json())
