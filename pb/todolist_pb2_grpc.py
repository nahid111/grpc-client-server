# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import todolist_pb2 as todolist__pb2


class TodoListStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AddTodo = channel.unary_unary(
                '/todolist.TodoList/AddTodo',
                request_serializer=todolist__pb2.Todo.SerializeToString,
                response_deserializer=todolist__pb2.TodoResponse.FromString,
                )
        self.GetTodos = channel.unary_unary(
                '/todolist.TodoList/GetTodos',
                request_serializer=todolist__pb2.Empty.SerializeToString,
                response_deserializer=todolist__pb2.TodoListResponse.FromString,
                )
        self.DeleteTodo = channel.unary_unary(
                '/todolist.TodoList/DeleteTodo',
                request_serializer=todolist__pb2.DeleteTodoRequest.SerializeToString,
                response_deserializer=todolist__pb2.TodoResponse.FromString,
                )


class TodoListServicer(object):
    """Missing associated documentation comment in .proto file."""

    def AddTodo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTodos(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteTodo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TodoListServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AddTodo': grpc.unary_unary_rpc_method_handler(
                    servicer.AddTodo,
                    request_deserializer=todolist__pb2.Todo.FromString,
                    response_serializer=todolist__pb2.TodoResponse.SerializeToString,
            ),
            'GetTodos': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTodos,
                    request_deserializer=todolist__pb2.Empty.FromString,
                    response_serializer=todolist__pb2.TodoListResponse.SerializeToString,
            ),
            'DeleteTodo': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteTodo,
                    request_deserializer=todolist__pb2.DeleteTodoRequest.FromString,
                    response_serializer=todolist__pb2.TodoResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'todolist.TodoList', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TodoList(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def AddTodo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/todolist.TodoList/AddTodo',
            todolist__pb2.Todo.SerializeToString,
            todolist__pb2.TodoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTodos(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/todolist.TodoList/GetTodos',
            todolist__pb2.Empty.SerializeToString,
            todolist__pb2.TodoListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteTodo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/todolist.TodoList/DeleteTodo',
            todolist__pb2.DeleteTodoRequest.SerializeToString,
            todolist__pb2.TodoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
