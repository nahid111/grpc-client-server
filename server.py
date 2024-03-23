import grpc
from concurrent import futures
from pb import todolist_pb2
from pb import todolist_pb2_grpc


class TodoListServicer(todolist_pb2_grpc.TodoListServicer):
    def __init__(self):
        self.todos = []
        self.counter = 1

    def AddTodo(self, request, context):
        todo = todolist_pb2.Todo(
            id=self.counter,
            title=request.title,
            description=request.description
        )
        self.todos.append(todo)
        self.counter += 1
        return todolist_pb2.TodoResponse(todo=todo, message="Todo added successfully")

    def GetTodos(self, request, context):
        return todolist_pb2.TodoListResponse(todos=self.todos)

    def DeleteTodo(self, request, context):
        for todo in self.todos:
            if todo.id == request.id:
                self.todos.remove(todo)
                return todolist_pb2.TodoResponse(todo=todo, message="Todo deleted successfully")
        return todolist_pb2.TodoResponse(message="Todo not found")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    todolist_pb2_grpc.add_TodoListServicer_to_server(
        TodoListServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started...")
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
