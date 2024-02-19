import grpc
import protos.holamundo_pb2
import protos.holamundo_pb2_grpc

def run():
    print(" Intentando decir hola")
    with grpc.insecure_channel("localhost:50501") as channel:
        stub = holamundo_pb2_grpc.SaludadorStub()
        respuesta = stub.diHola(holamundo_pb2.HelloRequest(name="Octavio"))
        print("El cliente recibio", respuesta.message)

if __name__ == "__main__":
    run()