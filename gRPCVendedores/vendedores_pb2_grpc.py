# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import vendedores_pb2 as vendedores__pb2


class ComunicadorStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Registro_Vendedor = channel.unary_unary(
                '/Comunicaciones.Comunicador/Registro_Vendedor',
                request_serializer=vendedores__pb2.RegistroVendedor.SerializeToString,
                response_deserializer=vendedores__pb2.Status.FromString,
                )
        self.Registro_Tienda = channel.unary_unary(
                '/Comunicaciones.Comunicador/Registro_Tienda',
                request_serializer=vendedores__pb2.RegistroTienda.SerializeToString,
                response_deserializer=vendedores__pb2.Status.FromString,
                )
        self.Registro_Asignacion = channel.unary_unary(
                '/Comunicaciones.Comunicador/Registro_Asignacion',
                request_serializer=vendedores__pb2.RegistroAsignacion.SerializeToString,
                response_deserializer=vendedores__pb2.Status.FromString,
                )
        self.listador_tiendas = channel.unary_stream(
                '/Comunicaciones.Comunicador/listador_tiendas',
                request_serializer=vendedores__pb2.Empty.SerializeToString,
                response_deserializer=vendedores__pb2.RegistroTienda.FromString,
                )
        self.listador_asignaciones = channel.unary_stream(
                '/Comunicaciones.Comunicador/listador_asignaciones',
                request_serializer=vendedores__pb2.Empty.SerializeToString,
                response_deserializer=vendedores__pb2.RegistroAsignacion.FromString,
                )
        self.agregador = channel.stream_unary(
                '/Comunicaciones.Comunicador/agregador',
                request_serializer=vendedores__pb2.Producto.SerializeToString,
                response_deserializer=vendedores__pb2.Status.FromString,
                )
        self.listador_productos = channel.unary_stream(
                '/Comunicaciones.Comunicador/listador_productos',
                request_serializer=vendedores__pb2.Empty.SerializeToString,
                response_deserializer=vendedores__pb2.Producto.FromString,
                )


class ComunicadorServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Registro_Vendedor(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Registro_Tienda(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Registro_Asignacion(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def listador_tiendas(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def listador_asignaciones(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def agregador(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def listador_productos(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ComunicadorServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Registro_Vendedor': grpc.unary_unary_rpc_method_handler(
                    servicer.Registro_Vendedor,
                    request_deserializer=vendedores__pb2.RegistroVendedor.FromString,
                    response_serializer=vendedores__pb2.Status.SerializeToString,
            ),
            'Registro_Tienda': grpc.unary_unary_rpc_method_handler(
                    servicer.Registro_Tienda,
                    request_deserializer=vendedores__pb2.RegistroTienda.FromString,
                    response_serializer=vendedores__pb2.Status.SerializeToString,
            ),
            'Registro_Asignacion': grpc.unary_unary_rpc_method_handler(
                    servicer.Registro_Asignacion,
                    request_deserializer=vendedores__pb2.RegistroAsignacion.FromString,
                    response_serializer=vendedores__pb2.Status.SerializeToString,
            ),
            'listador_tiendas': grpc.unary_stream_rpc_method_handler(
                    servicer.listador_tiendas,
                    request_deserializer=vendedores__pb2.Empty.FromString,
                    response_serializer=vendedores__pb2.RegistroTienda.SerializeToString,
            ),
            'listador_asignaciones': grpc.unary_stream_rpc_method_handler(
                    servicer.listador_asignaciones,
                    request_deserializer=vendedores__pb2.Empty.FromString,
                    response_serializer=vendedores__pb2.RegistroAsignacion.SerializeToString,
            ),
            'agregador': grpc.stream_unary_rpc_method_handler(
                    servicer.agregador,
                    request_deserializer=vendedores__pb2.Producto.FromString,
                    response_serializer=vendedores__pb2.Status.SerializeToString,
            ),
            'listador_productos': grpc.unary_stream_rpc_method_handler(
                    servicer.listador_productos,
                    request_deserializer=vendedores__pb2.Empty.FromString,
                    response_serializer=vendedores__pb2.Producto.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Comunicaciones.Comunicador', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Comunicador(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Registro_Vendedor(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Comunicaciones.Comunicador/Registro_Vendedor',
            vendedores__pb2.RegistroVendedor.SerializeToString,
            vendedores__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Registro_Tienda(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Comunicaciones.Comunicador/Registro_Tienda',
            vendedores__pb2.RegistroTienda.SerializeToString,
            vendedores__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Registro_Asignacion(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Comunicaciones.Comunicador/Registro_Asignacion',
            vendedores__pb2.RegistroAsignacion.SerializeToString,
            vendedores__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def listador_tiendas(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/Comunicaciones.Comunicador/listador_tiendas',
            vendedores__pb2.Empty.SerializeToString,
            vendedores__pb2.RegistroTienda.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def listador_asignaciones(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/Comunicaciones.Comunicador/listador_asignaciones',
            vendedores__pb2.Empty.SerializeToString,
            vendedores__pb2.RegistroAsignacion.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def agregador(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/Comunicaciones.Comunicador/agregador',
            vendedores__pb2.Producto.SerializeToString,
            vendedores__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def listador_productos(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/Comunicaciones.Comunicador/listador_productos',
            vendedores__pb2.Empty.SerializeToString,
            vendedores__pb2.Producto.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
