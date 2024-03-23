# [GRPC](https://grpc.io/docs/languages/go/quickstart/)-ToDoList

A simple grpc client-server example with a python server and a go client

## installation

- install python dependencies

  ```bash
  $ pip install -r requirements.txt
  ```

- install go dependencies

  ```bash
  $ go mod tidy
  ```

## Run

- Run server

  ```bash
  $ python server.py
  ```

- Run Client

  ```bash
  $ go run client.go
  ```

## Modifying

Regenerate the pb files after modifying the `./protos/todolist.proto` file

- Generate grpc `python` code

  ```bash
  $ python -m grpc_tools.protoc -I ./protos --python_out=./pb/ --pyi_out=./pb/ --grpc_python_out=./pb/ ./protos/todolist.proto
  ```

- Generate grpc `go` code

  - You need to have [Protocol Buffer Compiler](https://grpc.io/docs/protoc-installation/) pre-installed

    ```bash
    $ export PATH="$PATH:$(go env GOPATH)/bin"

    $ protoc --go_out=. --go-grpc_out=. ./protos/todolist.proto
    ```
