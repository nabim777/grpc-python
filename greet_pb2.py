# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: greet.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bgreet.proto\x12\x05greet\"\x1c\n\x0cHelloRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"!\n\rHelloResponse\x12\x10\n\x08greeting\x18\x01 \x01(\t2H\n\x0fGreetingService\x12\x35\n\x08SayHello\x12\x13.greet.HelloRequest\x1a\x14.greet.HelloResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'greet_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_HELLOREQUEST']._serialized_start=22
  _globals['_HELLOREQUEST']._serialized_end=50
  _globals['_HELLORESPONSE']._serialized_start=52
  _globals['_HELLORESPONSE']._serialized_end=85
  _globals['_GREETINGSERVICE']._serialized_start=87
  _globals['_GREETINGSERVICE']._serialized_end=159
# @@protoc_insertion_point(module_scope)
