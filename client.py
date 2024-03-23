
import pprint
import grpc
from pb import todolist_pb2
from pb import todolist_pb2_grpc
import json


def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = todolist_pb2_grpc.TodoListStub(channel)

    # define todos
    todo1 = todolist_pb2.Todo(title="Buy groceries", description="Milk, Bread")
    todo2 = todolist_pb2.Todo(title="Study", description="Math, Physics")
    todo_empty = todolist_pb2.Empty()

    # Call procedures

    res1 = stub.AddTodo(todo1)
    print("AddTodo:", res1.message)

    
    res2 = stub.AddTodo(todo2)
    print("AddTodo:", res2.message)

    todos = stub.GetTodos(todo_empty)
    print("\nTodos:")
    for todo in todos.todos:
        print(todo.title, "-", todo.description)

    res = stub.DeleteTodo(todolist_pb2.DeleteTodoRequest(id=1))
    print("DeleteTodo:", res.message)

    todos = stub.GetTodos(todo_empty)
    print("\nTodos:")
    for todo in todos.todos:
        print(todo.title, "-", todo.description)


if __name__ == '__main__':
    run()
