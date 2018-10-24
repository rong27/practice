from concurrent import futures
import time

import grpc
import hello_pb2
import hello_pb2_grpc

import hello

class HelloServicer(hello_pb2_grpc.HelloServicer):
    def Hello(self,request,context):
        response = hello_pb2.HelloResponse()
        response.value = hello.hello(request.value)
        return response

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hello_pb2_grpc.add_HelloServicer_to_server(HelloServicer(),server)