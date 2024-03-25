from concurrent import futures
import grpc
import administracion_pb2
import administracion_pb2_grpc

class Administrador (administracion_pb2_grpc.AdministracionServicer):
    folio_vendedores = 0
    folio_productos = 0
    folio_tiendas = 0
    folio_asignaciones = 0
    vendedores = {}
    tiendas = {}
    productos = {}
    asignaciones = {}

    def registrar_vendedor(self, request, context): # (RegistroVendedor) 
        Administrador.folio_vendedores += 1 
        Administrador.vendedores[Administrador.folio_vendedores] = administracion_pb2.RegistroVendedor(id=Administrador.folio_vendedores, nombre=request.nombre, edad=request.edad, salario=request.salario)
        for vendedor in Administrador.vendedores.values(): 
            print(len(Administrador.vendedores.values()), type(vendedor), vendedor)
        return administracion_pb2.Status(success=True)
    
    def registrar_tienda(self, request, context): # (RegistroTienda) 
        Administrador.folio_tiendas += 1 
        Administrador.tiendas[Administrador.folio_tiendas] = administracion_pb2.RegistroTienda(id=Administrador.folio_tiendas, descripcion=request.descripcion, delegacion=request.delegacion)
        for tienda in Administrador.tiendas.values(): 
            print(len(Administrador.tiendas.values()), type(tienda), tienda)
        return administracion_pb2.Status(success=True)

    def asignar_a_tienda(self, request, context): # (SolicitudAsignacion) 
        try:
            Administrador.vendedores[request.id_vendedor] 
            Administrador.tiendas[request.id_tienda]
            Administrador.folio_asignaciones += 1
            Administrador.asignaciones[Administrador.folio_asignaciones] = administracion_pb2.RegistroAsignacion(id=Administrador.folio_asignaciones, id_tienda = request.id_tienda)
            for asignacion in Administrador.asignaciones.values(): 
                print(len(Administrador.asignaciones.values()), type(asignacion), asignacion)
            return administracion_pb2.Status(success=True)
        except:
            return administracion_pb2.Status(success=False)
            
    
    def listado_tiendas(self, request, context): # (Empty)   
        for tienda in Administrador.tiendas.values(): 
            yield tienda

    def listado_productos(self, request, context): # (Empty)   
        for producto in Administrador.productos.values(): 
            yield producto

    def listado_vendedores(self, request, context): # (Empty) 
        for vendedor in Administrador.vendedores.values(): 
            yield vendedor

    def listado_asignaciones(self, request, context): # (Empty) 
        mis_asignaciones = []
        for asignacion in Administrador.asignaciones.values(): 
             mis_asignaciones.append(asignacion)
        return administracion_pb2.ListadoAsignaciones(asignaciones=mis_asignaciones)

    def agrega_productos(self, request_iterator, context):
        for producto in request_iterator: 
            Administrador.folio_productos += 1 
            Administrador.productos[Administrador.folio_productos] = administracion_pb2.Producto(id=Administrador.folio_productos, 
                                                                                                 cantidad=producto.cantidad, 
                                                                                                 descripcion=producto.descripcion)
        return administracion_pb2.Status(success=True)


def ofrece_servicios():
    puerto = "50051"
    servidor = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    administracion_pb2_grpc.add_AdministracionServicer_to_server(Administrador(), servidor)
    servidor.add_insecure_port("[::]:" + puerto)
    servidor.start()
    servidor.wait_for_termination()

if __name__ == "__main__":
    print("Ofreciendo servicios de administración")
    ofrece_servicios()
    