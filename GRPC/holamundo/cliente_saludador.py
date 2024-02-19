import grpc
import GRPC.holamundo.holamundo_pb2 as hm_pb2
import GRPC.holamundo.holamundo_pb2_grpc as hm_pb2_grpc

def run():
    print(" Intentando decir hola")
    with grpc.insecure_channel("localhost:50501") as channel:
        stub = hm_pb2_grpc.SaludadorStub()
        respuesta = stub.diHola(hm_pb2.HelloRequest(name="Octavio"))
        print("El cliente recibio", respuesta.message)

if __name__ == "__main__":
    run()