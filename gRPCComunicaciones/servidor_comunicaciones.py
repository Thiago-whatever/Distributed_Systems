from concurrent import futures
import grpc
import comunicaciones_pb2_grpc
import comunicaciones_pb2

class Comunicador(comunicaciones_pb2_grpc.ComunicadorServicer):
    folio = 0
    elementos = {} #diccionario de elementos (base de datos)

    
    def listador_elementos1(self, request, context):
        #Implementacion para que nos regrese un stream

        #Para que me regrese todos los valores asociados
        #En cada iteracion va a enviar el siguiente objeto
        #hasta terminar de enviar todo
        for elemento in Comunicador.elementos.values:
            yield elemento #Cada que tenga un stream tengo que usar yield
        pass

    def listador_elementos2(self, request, context):
        listado = [] #Poblar lista con todos los elementos

        for elemento in Comunicador.elementos.values:
            listado.append(elemento)

        return comunicaciones_pb2.ListadoElementos(objetos = listado)
        pass

    def agregador(self, request_iterator, context):
        pass