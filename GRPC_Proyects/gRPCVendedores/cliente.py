import grpc
import administracion_pb2
import administracion_pb2_grpc

def generador_productos(productos):
    for producto in productos:
        yield administracion_pb2.Producto(cantidad=producto[0], descripcion=producto[1]) 

def run():
    print("Intentando registrar")
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = administracion_pb2_grpc.AdministracionStub(channel)
        stub.registrar_vendedor(administracion_pb2.RegistroVendedor(nombre="Pedro", edad=80, salario=40000))
        stub.registrar_vendedor(administracion_pb2.RegistroVendedor(nombre="Juana", edad=40, salario=20000))
        stub.registrar_tienda(administracion_pb2.RegistroTienda(descripcion="Sur", delegacion="Xochimilco"))
        stub.registrar_tienda(administracion_pb2.RegistroTienda(descripcion="Oeste", delegacion="Álvaro Obregón"))        
        stub.asignar_a_tienda(administracion_pb2.RegistroAsignacion(id_vendedor=1, id_tienda=1))
        stub.asignar_a_tienda(administracion_pb2.RegistroAsignacion(id_vendedor=2, id_tienda=2))
        iterador_productos = generador_productos([(10, "producto 1"), (20, "producto 2")])
        stub.agrega_productos(iterador_productos)

        listado = stub.listado_asignaciones(administracion_pb2.Empty())
        for asignacion in listado.asignaciones:
            print("Asignacion: ", asignacion)

        for vendedor in stub.listado_vendedores(administracion_pb2.Empty()):
            print(vendedor.id, "Nombre:", vendedor.nombre, "Edad:", vendedor.salario)
        
        for tienda in stub.listado_tiendas(administracion_pb2.Empty()):
            print(tienda.id, "Tienda:", tienda.descripcion, "Delegación:", tienda.delegacion)
        
        for producto in stub.listado_productos(administracion_pb2.Empty()):
            print(producto.id, "Cantidad:", producto.cantidad, "Descripcion:", producto.descripcion)


if __name__ == "__main__":
    run()