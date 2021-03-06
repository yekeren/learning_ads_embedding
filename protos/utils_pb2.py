# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/utils.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from object_detection.protos import hyperparams_pb2 as object__detection_dot_protos_dot_hyperparams__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='protos/utils.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x12protos/utils.proto\x1a)object_detection/protos/hyperparams.proto\"\xc7\x01\n\tFCEncoder\x12\x19\n\x05scope\x18\x01 \x01(\t:\nfc_encoder\x12\x18\n\x0bnum_outputs\x18\x02 \x01(\x05:\x03\x32\x30\x30\x12\"\n\x17input_dropout_keep_prob\x18\x03 \x01(\x02:\x01\x31\x12#\n\x18output_dropout_keep_prob\x18\x04 \x01(\x02:\x01\x31\x12<\n\x0e\x66\x63_hyperparams\x18\x05 \x01(\x0b\x32$.object_detection.protos.Hyperparams')
  ,
  dependencies=[object__detection_dot_protos_dot_hyperparams__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_FCENCODER = _descriptor.Descriptor(
  name='FCEncoder',
  full_name='FCEncoder',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='scope', full_name='FCEncoder.scope', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("fc_encoder").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_outputs', full_name='FCEncoder.num_outputs', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=200,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='input_dropout_keep_prob', full_name='FCEncoder.input_dropout_keep_prob', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(1),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='output_dropout_keep_prob', full_name='FCEncoder.output_dropout_keep_prob', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(1),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fc_hyperparams', full_name='FCEncoder.fc_hyperparams', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=66,
  serialized_end=265,
)

_FCENCODER.fields_by_name['fc_hyperparams'].message_type = object__detection_dot_protos_dot_hyperparams__pb2._HYPERPARAMS
DESCRIPTOR.message_types_by_name['FCEncoder'] = _FCENCODER

FCEncoder = _reflection.GeneratedProtocolMessageType('FCEncoder', (_message.Message,), dict(
  DESCRIPTOR = _FCENCODER,
  __module__ = 'protos.utils_pb2'
  # @@protoc_insertion_point(class_scope:FCEncoder)
  ))
_sym_db.RegisterMessage(FCEncoder)


# @@protoc_insertion_point(module_scope)
