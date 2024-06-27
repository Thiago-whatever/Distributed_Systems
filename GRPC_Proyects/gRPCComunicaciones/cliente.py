from concurrent import futures
import grpc
import comunicaciones_pb2_grpc
import comunicaciones_pb2

def generador_elementos (elementos):
    for elemento in elementos:
        yield comunicaciones_pb2.Elemento(descripcion=elemento)


def run():
    print("Intentando agregar y consultar elementos")
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = comunicaciones_pb2_grpc.ComunicadorStub(channel)

        #e.g., consulta de SQL
        iterador_elementos = generador_elementos(["Elemento A","Elemento B", "Elemento C"])
        respuesta = stub.agregador(iterador_elementos)
        print("Resultadode agregar: ", respuesta.success)

        for elemento in stub.listador_elementos1(comunicaciones_pb2.Empty()):
            print("elemento id" + str(elemento.id) + "descripcion: "+ elemento.descripcion)
        
        listado = stub.listador_elementos2(comunicaciones_pb2.Empty())
        for elemento in listado.objetos:
            print("Elemento", elemento)


if __name__ == "__main__":
    run()
