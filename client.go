package main

import (
	"context"
	"log"

	"google.golang.org/grpc"
	"grpc-client-server/pb" // Import the generated package
)

func main() {
	// Set up a connection to the server
	conn, err := grpc.Dial("localhost:50051", grpc.WithInsecure())
	if err != nil {
		log.Fatalf("Failed to dial server: %v", err)
	}
	defer conn.Close()

	// Create a TodoList client
	client := pb.NewTodoListClient(conn)

	// Call AddTodo RPC
	todo := &pb.Todo{
		Id:          1,
		Title:       "Sample Todo",
		Description: "This is a sample todo.",
	}
	addResponse, err := client.AddTodo(context.Background(), todo)
	if err != nil {
		log.Fatalf("AddTodo failed: %v", err)
	}
	log.Printf("AddTodo Response: %v", addResponse)

	// Call GetTodos RPC
	getResponse, err := client.GetTodos(context.Background(), &pb.Empty{})
	if err != nil {
		log.Fatalf("GetTodos failed: %v", err)
	}
	log.Printf("GetTodos Response: %v", getResponse)

	// Call DeleteTodo RPC
	deleteResponse, err := client.DeleteTodo(context.Background(), &pb.DeleteTodoRequest{Id: 1})
	if err != nil {
		log.Fatalf("DeleteTodo failed: %v", err)
	}
	log.Printf("DeleteTodo Response: %v", deleteResponse)
}
