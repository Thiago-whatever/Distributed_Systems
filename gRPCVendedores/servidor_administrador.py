from concurrent import futures
import grpc
import vendedores_pb2_grpc
import vendedores_pb2

class Servidor(vendedores_pb2_grpc.ComunicadorServicer):
    folio_vendedores = 0
    folio_productos = 0
    folio_tiendas = 0
    folio_asignaciones = 0
    vendedores = {}
    tiendas = {}
    productos = {}
    asignaciones = {}

    def Registro_Vendedor(self, request, context):
        Servidor.folio_vendedores += 1
        Servidor.vendedores[Servidor.folio_vendedores] = vendedores_pb2.RegistroVendedor(
            id = Servidor.folio_vendedores,
            nombre= request.nombre,
            edad = request.edad,
            salario = request.salario)
        return vendedores_pb2.Status(success=True)
        
    def Registro_Tienda(self, request, context):
        Servidor.folio_tiendas += 1
        Servidor.tiendas[Servidor.folio_tiendas] = vendedores_pb2.RegistroTienda(
            id = Servidor.folio_tiendas,
            descripcion = request.descripcion,
            delegacion= request.delegacion)
        return vendedores_pb2.Status(success=True)
    
    def Registro_Asignacion(self, request, context):
        Servidor.folio_asignaciones += 1
        Servidor.vendedores[Servidor.folio_asignaciones] = vendedores_pb2.RegistroTienda(
            idAsignacion = Servidor.folio_asignaciones,
            idTienda = request.idTienda,
            idVendedor= request.idVendedor)
        return vendedores_pb2.Status(success=True)

    def listador_tiendas(self, request, context):
        for elemento in Servidor.tiendas.values():
            yield elemento

    def listador_asignaciones(self, request, context):
        for elemento in Servidor.asignaciones.values():
            yield elemento
    
    def listador_productos(self, request, context):
        for elemento in Servidor.productos.values():
            yield elemento

    def agregador(self, request_iterator, context):
        for elemento in request_iterator:
            Servidor.folio_productos += 1
            Servidor.productos[Servidor.folio_productos] = vendedores_pb2.Producto(
                id = Servidor.folio_productos,
                cantidad = elemento.cantidad,
                descripcion= elemento.descripcion)
        for elemento in Servidor.productos.values:
            print(elemento, elemento.id, elemento.cantidad, elemento.descripcion)

        return vendedores_pb2.Status(success=True)
    
def run():
    print("hola mundo")

if __name__ == "__main__":
    run()