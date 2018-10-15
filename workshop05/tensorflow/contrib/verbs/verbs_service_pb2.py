# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow/contrib/verbs/verbs_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='tensorflow/contrib/verbs/verbs_service.proto',
  package='tensorflow',
  syntax='proto3',
  serialized_options=_b('\n\034org.tensorflow.contrib.verbsB\022VerbsServiceProtosP\001'),
  serialized_pb=_b('\n,tensorflow/contrib/verbs/verbs_service.proto\x12\ntensorflow\"J\n\x07\x43hannel\x12\x0b\n\x03lid\x18\x01 \x01(\x05\x12\x0b\n\x03qpn\x18\x02 \x01(\x05\x12\x0b\n\x03psn\x18\x03 \x01(\x05\x12\x0b\n\x03snp\x18\x04 \x01(\x04\x12\x0b\n\x03iid\x18\x05 \x01(\x04\"1\n\x0cMemoryRegion\x12\x13\n\x0bremote_addr\x18\x01 \x01(\x04\x12\x0c\n\x04rkey\x18\x02 \x01(\r\"x\n\x17GetRemoteAddressRequest\x12\x11\n\thost_name\x18\x01 \x01(\t\x12$\n\x07\x63hannel\x18\x02 \x01(\x0b\x32\x13.tensorflow.Channel\x12$\n\x02mr\x18\x03 \x03(\x0b\x32\x18.tensorflow.MemoryRegion\"y\n\x18GetRemoteAddressResponse\x12\x11\n\thost_name\x18\x01 \x01(\t\x12$\n\x07\x63hannel\x18\x02 \x01(\x0b\x32\x13.tensorflow.Channel\x12$\n\x02mr\x18\x03 \x03(\x0b\x32\x18.tensorflow.MemoryRegion\"T\n\x10\x45rrorStatusProto\x12\x12\n\nerror_code\x18\x01 \x01(\x05\x12\x15\n\rerror_message\x18\x02 \x01(\t\x12\x15\n\rerror_details\x18\x03 \x01(\t2m\n\x0cVerbsService\x12]\n\x10GetRemoteAddress\x12#.tensorflow.GetRemoteAddressRequest\x1a$.tensorflow.GetRemoteAddressResponseB4\n\x1corg.tensorflow.contrib.verbsB\x12VerbsServiceProtosP\x01\x62\x06proto3')
)




_CHANNEL = _descriptor.Descriptor(
  name='Channel',
  full_name='tensorflow.Channel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lid', full_name='tensorflow.Channel.lid', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='qpn', full_name='tensorflow.Channel.qpn', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='psn', full_name='tensorflow.Channel.psn', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='snp', full_name='tensorflow.Channel.snp', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='iid', full_name='tensorflow.Channel.iid', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=60,
  serialized_end=134,
)


_MEMORYREGION = _descriptor.Descriptor(
  name='MemoryRegion',
  full_name='tensorflow.MemoryRegion',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='remote_addr', full_name='tensorflow.MemoryRegion.remote_addr', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rkey', full_name='tensorflow.MemoryRegion.rkey', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=136,
  serialized_end=185,
)


_GETREMOTEADDRESSREQUEST = _descriptor.Descriptor(
  name='GetRemoteAddressRequest',
  full_name='tensorflow.GetRemoteAddressRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='host_name', full_name='tensorflow.GetRemoteAddressRequest.host_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='channel', full_name='tensorflow.GetRemoteAddressRequest.channel', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mr', full_name='tensorflow.GetRemoteAddressRequest.mr', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=187,
  serialized_end=307,
)


_GETREMOTEADDRESSRESPONSE = _descriptor.Descriptor(
  name='GetRemoteAddressResponse',
  full_name='tensorflow.GetRemoteAddressResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='host_name', full_name='tensorflow.GetRemoteAddressResponse.host_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='channel', full_name='tensorflow.GetRemoteAddressResponse.channel', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mr', full_name='tensorflow.GetRemoteAddressResponse.mr', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=309,
  serialized_end=430,
)


_ERRORSTATUSPROTO = _descriptor.Descriptor(
  name='ErrorStatusProto',
  full_name='tensorflow.ErrorStatusProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='error_code', full_name='tensorflow.ErrorStatusProto.error_code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error_message', full_name='tensorflow.ErrorStatusProto.error_message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error_details', full_name='tensorflow.ErrorStatusProto.error_details', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=432,
  serialized_end=516,
)

_GETREMOTEADDRESSREQUEST.fields_by_name['channel'].message_type = _CHANNEL
_GETREMOTEADDRESSREQUEST.fields_by_name['mr'].message_type = _MEMORYREGION
_GETREMOTEADDRESSRESPONSE.fields_by_name['channel'].message_type = _CHANNEL
_GETREMOTEADDRESSRESPONSE.fields_by_name['mr'].message_type = _MEMORYREGION
DESCRIPTOR.message_types_by_name['Channel'] = _CHANNEL
DESCRIPTOR.message_types_by_name['MemoryRegion'] = _MEMORYREGION
DESCRIPTOR.message_types_by_name['GetRemoteAddressRequest'] = _GETREMOTEADDRESSREQUEST
DESCRIPTOR.message_types_by_name['GetRemoteAddressResponse'] = _GETREMOTEADDRESSRESPONSE
DESCRIPTOR.message_types_by_name['ErrorStatusProto'] = _ERRORSTATUSPROTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Channel = _reflection.GeneratedProtocolMessageType('Channel', (_message.Message,), dict(
  DESCRIPTOR = _CHANNEL,
  __module__ = 'tensorflow.contrib.verbs.verbs_service_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.Channel)
  ))
_sym_db.RegisterMessage(Channel)

MemoryRegion = _reflection.GeneratedProtocolMessageType('MemoryRegion', (_message.Message,), dict(
  DESCRIPTOR = _MEMORYREGION,
  __module__ = 'tensorflow.contrib.verbs.verbs_service_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.MemoryRegion)
  ))
_sym_db.RegisterMessage(MemoryRegion)

GetRemoteAddressRequest = _reflection.GeneratedProtocolMessageType('GetRemoteAddressRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETREMOTEADDRESSREQUEST,
  __module__ = 'tensorflow.contrib.verbs.verbs_service_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.GetRemoteAddressRequest)
  ))
_sym_db.RegisterMessage(GetRemoteAddressRequest)

GetRemoteAddressResponse = _reflection.GeneratedProtocolMessageType('GetRemoteAddressResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETREMOTEADDRESSRESPONSE,
  __module__ = 'tensorflow.contrib.verbs.verbs_service_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.GetRemoteAddressResponse)
  ))
_sym_db.RegisterMessage(GetRemoteAddressResponse)

ErrorStatusProto = _reflection.GeneratedProtocolMessageType('ErrorStatusProto', (_message.Message,), dict(
  DESCRIPTOR = _ERRORSTATUSPROTO,
  __module__ = 'tensorflow.contrib.verbs.verbs_service_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.ErrorStatusProto)
  ))
_sym_db.RegisterMessage(ErrorStatusProto)


DESCRIPTOR._options = None

_VERBSSERVICE = _descriptor.ServiceDescriptor(
  name='VerbsService',
  full_name='tensorflow.VerbsService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=518,
  serialized_end=627,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetRemoteAddress',
    full_name='tensorflow.VerbsService.GetRemoteAddress',
    index=0,
    containing_service=None,
    input_type=_GETREMOTEADDRESSREQUEST,
    output_type=_GETREMOTEADDRESSRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_VERBSSERVICE)

DESCRIPTOR.services_by_name['VerbsService'] = _VERBSSERVICE

# @@protoc_insertion_point(module_scope)
