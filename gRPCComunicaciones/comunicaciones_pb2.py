# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: comunicaciones.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14\x63omunicaciones.proto\x12\x0e\x43omunicaciones\"\x07\n\x05\x45mpty\"*\n\x06Status\x12\x14\n\x07success\x18\x01 \x01(\x08H\x00\x88\x01\x01\x42\n\n\x08_success\"L\n\x08\x45lemento\x12\x0f\n\x02id\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12\x18\n\x0b\x64\x65scripcion\x18\x02 \x01(\tH\x01\x88\x01\x01\x42\x05\n\x03_idB\x0e\n\x0c_descripcion\"=\n\x10ListadoElementos\x12)\n\x07objetos\x18\x01 \x03(\x0b\x32\x18.Comunicaciones.Elemento2\xee\x01\n\x0b\x43omunicador\x12J\n\x13listador_elementos1\x12\x15.Comunicaciones.Empty\x1a\x18.Comunicaciones.Elemento\"\x00\x30\x01\x12P\n\x13listador_elementos2\x12\x15.Comunicaciones.Empty\x1a .Comunicaciones.ListadoElementos\"\x00\x12\x41\n\tagregador\x12\x18.Comunicaciones.Elemento\x1a\x16.Comunicaciones.Status\"\x00(\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'comunicaciones_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_EMPTY']._serialized_start=40
  _globals['_EMPTY']._serialized_end=47
  _globals['_STATUS']._serialized_start=49
  _globals['_STATUS']._serialized_end=91
  _globals['_ELEMENTO']._serialized_start=93
  _globals['_ELEMENTO']._serialized_end=169
  _globals['_LISTADOELEMENTOS']._serialized_start=171
  _globals['_LISTADOELEMENTOS']._serialized_end=232
  _globals['_COMUNICADOR']._serialized_start=235
  _globals['_COMUNICADOR']._serialized_end=473
# @@protoc_insertion_point(module_scope)
