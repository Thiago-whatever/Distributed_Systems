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

    def listador_elementos2(self, request, context):
        listado = [] #Poblar lista con todos los elementos

        for elemento in Comunicador.elementos.values:
            listado.append(elemento)

        return comunicaciones_pb2.ListadoElementos(objetos = listado)
        

    def agregador(self, request_iterator, context):
        #No se espera a que el cliente empuje todos
        #mientras los está enviando, los va empujando
        for elemento in request_iterator:
            Comunicador.folio += 1
            Comunicador.elementos[Comunicador.folio] = comunicaciones_pb2.Elemento(
                id =  Comunicador.folio,
                descripcion = elemento.descripcion)
        return comunicaciones_pb2.Status(success=True)
    
def run():
    puerto = "50051"
    servidor = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    comunicaciones_pb2_grpc.add_ComunicadorServicer_to_server(Comunicador(),servidor)
    servidor.add_insecure_port("[::]:"+puerto)
    print("Arrancando servidor:")
    servidor.start()
    servidor.wait_for_termination()
        
if __name__ == "main":
    run()