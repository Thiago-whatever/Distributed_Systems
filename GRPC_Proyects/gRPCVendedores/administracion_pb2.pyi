from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Empty(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Status(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...

class Producto(_message.Message):
    __slots__ = ("id", "cantidad", "descripcion")
    ID_FIELD_NUMBER: _ClassVar[int]
    CANTIDAD_FIELD_NUMBER: _ClassVar[int]
    DESCRIPCION_FIELD_NUMBER: _ClassVar[int]
    id: int
    cantidad: int
    descripcion: str
    def __init__(self, id: _Optional[int] = ..., cantidad: _Optional[int] = ..., descripcion: _Optional[str] = ...) -> None: ...

class RegistroVendedor(_message.Message):
    __slots__ = ("id", "nombre", "edad", "salario")
    ID_FIELD_NUMBER: _ClassVar[int]
    NOMBRE_FIELD_NUMBER: _ClassVar[int]
    EDAD_FIELD_NUMBER: _ClassVar[int]
    SALARIO_FIELD_NUMBER: _ClassVar[int]
    id: int
    nombre: str
    edad: int
    salario: float
    def __init__(self, id: _Optional[int] = ..., nombre: _Optional[str] = ..., edad: _Optional[int] = ..., salario: _Optional[float] = ...) -> None: ...

class RegistroTienda(_message.Message):
    __slots__ = ("id", "descripcion", "delegacion")
    ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPCION_FIELD_NUMBER: _ClassVar[int]
    DELEGACION_FIELD_NUMBER: _ClassVar[int]
    id: int
    descripcion: str
    delegacion: str
    def __init__(self, id: _Optional[int] = ..., descripcion: _Optional[str] = ..., delegacion: _Optional[str] = ...) -> None: ...

class RegistroAsignacion(_message.Message):
    __slots__ = ("id", "id_vendedor", "id_tienda")
    ID_FIELD_NUMBER: _ClassVar[int]
    ID_VENDEDOR_FIELD_NUMBER: _ClassVar[int]
    ID_TIENDA_FIELD_NUMBER: _ClassVar[int]
    id: int
    id_vendedor: int
    id_tienda: int
    def __init__(self, id: _Optional[int] = ..., id_vendedor: _Optional[int] = ..., id_tienda: _Optional[int] = ...) -> None: ...

class ListadoAsignaciones(_message.Message):
    __slots__ = ("asignaciones",)
    ASIGNACIONES_FIELD_NUMBER: _ClassVar[int]
    asignaciones: _containers.RepeatedCompositeFieldContainer[RegistroAsignacion]
    def __init__(self, asignaciones: _Optional[_Iterable[_Union[RegistroAsignacion, _Mapping]]] = ...) -> None: ...
