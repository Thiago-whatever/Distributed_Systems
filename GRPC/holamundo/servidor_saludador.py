from concurrent import futures
import grpc 
import holamundo_pb2
import holamundo_pb2_grpc #el contenedor

class Saludador(holamundo_pb2_grpc.SaludadorServicer):
    
    def diHola(self,request,context):
        return holamundo_pb2.HelloReply(message="Hola %s" % request.name)
    
    def ofrece_servicio():
        puerto = "50501"
        servidor = grpc.server(futures.ThreadPoolExecuter(max_workers=10))
        holamundo_pb2_grpc.add_SaludadorServicer_to_server(Saludador(), servidor) #le pasamos una instancia de nuestra clase al contenedor
        #y lo vinculamos al servidor

        #[::] equivale a decir localhost --> servidor local, solo lo pueden acceder clientes dentro de la computadora
        servidor.add_insecure_port("[::]:" + puerto)

        #Para tener un servidor abierto tendria que tener "145.2.5.123:5050" --> tengo que poner en el cliente el IP

        servidor.start()
        print("El servidor esta arriba")
        servidor.wait_for_termination() #se queda como un daemon

    if __name__ == "main":
        ofrece_servicio()