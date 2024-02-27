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
    __slots__ = ("idAsignacion", "idTienda", "idVendedor")
    IDASIGNACION_FIELD_NUMBER: _ClassVar[int]
    IDTIENDA_FIELD_NUMBER: _ClassVar[int]
    IDVENDEDOR_FIELD_NUMBER: _ClassVar[int]
    idAsignacion: int
    idTienda: int
    idVendedor: int
    def __init__(self, idAsignacion: _Optional[int] = ..., idTienda: _Optional[int] = ..., idVendedor: _Optional[int] = ...) -> None: ...

class ListadoAsignaciones(_message.Message):
    __slots__ = ("objetos",)
    OBJETOS_FIELD_NUMBER: _ClassVar[int]
    objetos: _containers.RepeatedCompositeFieldContainer[RegistroAsignacion]
    def __init__(self, objetos: _Optional[_Iterable[_Union[RegistroAsignacion, _Mapping]]] = ...) -> None: ...
