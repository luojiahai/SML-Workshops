# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow/contrib/tpu/proto/tpu_embedding_config.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='tensorflow/contrib/tpu/proto/tpu_embedding_config.proto',
  package='tensorflow.tpu',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n7tensorflow/contrib/tpu/proto/tpu_embedding_config.proto\x12\x0etensorflow.tpu\"\xc0\x05\n\x19TPUEmbeddingConfiguration\x12G\n\nmodel_mode\x18\x01 \x01(\x0e\x32\x33.tensorflow.tpu.TPUEmbeddingConfiguration.ModelMode\x12\x11\n\tnum_hosts\x18\x02 \x01(\x05\x12\x17\n\x0fnum_tensornodes\x18\x03 \x01(\x05\x12\x12\n\nbatch_size\x18\x04 \x01(\x05\x12Q\n\x0ctable_config\x18\x05 \x03(\x0b\x32;.tensorflow.tpu.TPUEmbeddingConfiguration.TPUEmbeddingTable\x1a\x31\n\x18GradientDescentOptimizer\x12\x15\n\rlearning_rate\x18\x01 \x01(\x02\x1a\x46\n\x10\x41\x64\x61gradOptimizer\x12\x15\n\rlearning_rate\x18\x01 \x01(\x02\x12\x1b\n\x13initial_accumulator\x18\x02 \x01(\x02\x1a\x94\x02\n\x11TPUEmbeddingTable\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08num_rows\x18\x03 \x01(\x05\x12\r\n\x05width\x18\x04 \x01(\x05\x12\x14\n\x0cnum_features\x18\x05 \x01(\x05\x12^\n\x10gradient_descent\x18\x06 \x01(\x0b\x32\x42.tensorflow.tpu.TPUEmbeddingConfiguration.GradientDescentOptimizerH\x00\x12M\n\x07\x61\x64\x61grad\x18\x07 \x01(\x0b\x32:.tensorflow.tpu.TPUEmbeddingConfiguration.AdagradOptimizerH\x00\x42\x0b\n\toptimizer\"5\n\tModelMode\x12\x0b\n\x07INVALID\x10\x00\x12\x0c\n\x08TRAINING\x10\x01\x12\r\n\tINFERENCE\x10\x02\x62\x06proto3')
)



_TPUEMBEDDINGCONFIGURATION_MODELMODE = _descriptor.EnumDescriptor(
  name='ModelMode',
  full_name='tensorflow.tpu.TPUEmbeddingConfiguration.ModelMode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INVALID', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TRAINING', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INFERENCE', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=727,
  serialized_end=780,
)
_sym_db.RegisterEnumDescriptor(_TPUEMBEDDINGCONFIGURATION_MODELMODE)


_TPUEMBEDDINGCONFIGURATION_GRADIENTDESCENTOPTIMIZER = _descriptor.Descriptor(
  name='GradientDescentOptimizer',
  full_name='tensorflow.tpu.TPUEmbeddingConfiguration.GradientDescentOptimizer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='learning_rate', full_name='tensorflow.tpu.TPUEmbeddingConfiguration.GradientDescentOptimizer.learning_rate', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=325,
  serialized_end=374,
)

_TPUEMBEDDINGCONFIGURATION_ADAGRADOPTIMIZER = _descriptor.Descriptor(
  name='AdagradOptimizer',
  full_name='tensorflow.tpu.TPUEmbeddingConfiguration.AdagradOptimizer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='learning_rate', full_name='tensorflow.tpu.TPUEmbeddingConfiguration.AdagradOptimizer.learning_rate', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='initial_accumulator', full_name='tensorflow.tpu.TPUEmbeddingConfiguration.AdagradOptimizer.initial_accumulator', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=376,
  serialized_end=446,
)

_TPUEMBEDDINGCONFIGURATION_TPUEMBEDDINGTABLE = _descriptor.Descriptor(
  name='TPUEmbeddingTable',
  full_name='tensorflow.tpu.TPUEmbeddingConfiguration.TPUEmbeddingTable',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='tensorflow.tpu.TPUEmbeddingConfiguration.TPUEmbeddingTable.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_rows', full_name='tensorflow.tpu.TPUEmbeddingConfiguration.TPUEmbeddingTable.num_rows', index=1,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='width', full_name='tensorflow.tpu.TPUEmbeddingConfiguration.TPUEmbeddingTable.width', index=2,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_features', full_name='tensorflow.tpu.TPUEmbeddingConfiguration.TPUEmbeddingTable.num_features', index=3,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gradient_descent', full_name='tensorflow.tpu.TPUEmbeddingConfiguration.TPUEmbeddingTable.gradient_descent', index=4,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='adagrad', full_name='tensorflow.tpu.TPUEmbeddingConfiguration.TPUEmbeddingTable.adagrad', index=5,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
    _descriptor.OneofDescriptor(
      name='optimizer', full_name='tensorflow.tpu.TPUEmbeddingConfiguration.TPUEmbeddingTable.optimizer',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=449,
  serialized_end=725,
)

_TPUEMBEDDINGCONFIGURATION = _descriptor.Descriptor(
  name='TPUEmbeddingConfiguration',
  full_name='tensorflow.tpu.TPUEmbeddingConfiguration',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='model_mode', full_name='tensorflow.tpu.TPUEmbeddingConfiguration.model_mode', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_hosts', full_name='tensorflow.tpu.TPUEmbeddingConfiguration.num_hosts', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_tensornodes', full_name='tensorflow.tpu.TPUEmbeddingConfiguration.num_tensornodes', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='batch_size', full_name='tensorflow.tpu.TPUEmbeddingConfiguration.batch_size', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='table_config', full_name='tensorflow.tpu.TPUEmbeddingConfiguration.table_config', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_TPUEMBEDDINGCONFIGURATION_GRADIENTDESCENTOPTIMIZER, _TPUEMBEDDINGCONFIGURATION_ADAGRADOPTIMIZER, _TPUEMBEDDINGCONFIGURATION_TPUEMBEDDINGTABLE, ],
  enum_types=[
    _TPUEMBEDDINGCONFIGURATION_MODELMODE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=76,
  serialized_end=780,
)

_TPUEMBEDDINGCONFIGURATION_GRADIENTDESCENTOPTIMIZER.containing_type = _TPUEMBEDDINGCONFIGURATION
_TPUEMBEDDINGCONFIGURATION_ADAGRADOPTIMIZER.containing_type = _TPUEMBEDDINGCONFIGURATION
_TPUEMBEDDINGCONFIGURATION_TPUEMBEDDINGTABLE.fields_by_name['gradient_descent'].message_type = _TPUEMBEDDINGCONFIGURATION_GRADIENTDESCENTOPTIMIZER
_TPUEMBEDDINGCONFIGURATION_TPUEMBEDDINGTABLE.fields_by_name['adagrad'].message_type = _TPUEMBEDDINGCONFIGURATION_ADAGRADOPTIMIZER
_TPUEMBEDDINGCONFIGURATION_TPUEMBEDDINGTABLE.containing_type = _TPUEMBEDDINGCONFIGURATION
_TPUEMBEDDINGCONFIGURATION_TPUEMBEDDINGTABLE.oneofs_by_name['optimizer'].fields.append(
  _TPUEMBEDDINGCONFIGURATION_TPUEMBEDDINGTABLE.fields_by_name['gradient_descent'])
_TPUEMBEDDINGCONFIGURATION_TPUEMBEDDINGTABLE.fields_by_name['gradient_descent'].containing_oneof = _TPUEMBEDDINGCONFIGURATION_TPUEMBEDDINGTABLE.oneofs_by_name['optimizer']
_TPUEMBEDDINGCONFIGURATION_TPUEMBEDDINGTABLE.oneofs_by_name['optimizer'].fields.append(
  _TPUEMBEDDINGCONFIGURATION_TPUEMBEDDINGTABLE.fields_by_name['adagrad'])
_TPUEMBEDDINGCONFIGURATION_TPUEMBEDDINGTABLE.fields_by_name['adagrad'].containing_oneof = _TPUEMBEDDINGCONFIGURATION_TPUEMBEDDINGTABLE.oneofs_by_name['optimizer']
_TPUEMBEDDINGCONFIGURATION.fields_by_name['model_mode'].enum_type = _TPUEMBEDDINGCONFIGURATION_MODELMODE
_TPUEMBEDDINGCONFIGURATION.fields_by_name['table_config'].message_type = _TPUEMBEDDINGCONFIGURATION_TPUEMBEDDINGTABLE
_TPUEMBEDDINGCONFIGURATION_MODELMODE.containing_type = _TPUEMBEDDINGCONFIGURATION
DESCRIPTOR.message_types_by_name['TPUEmbeddingConfiguration'] = _TPUEMBEDDINGCONFIGURATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TPUEmbeddingConfiguration = _reflection.GeneratedProtocolMessageType('TPUEmbeddingConfiguration', (_message.Message,), dict(

  GradientDescentOptimizer = _reflection.GeneratedProtocolMessageType('GradientDescentOptimizer', (_message.Message,), dict(
    DESCRIPTOR = _TPUEMBEDDINGCONFIGURATION_GRADIENTDESCENTOPTIMIZER,
    __module__ = 'tensorflow.contrib.tpu.proto.tpu_embedding_config_pb2'
    # @@protoc_insertion_point(class_scope:tensorflow.tpu.TPUEmbeddingConfiguration.GradientDescentOptimizer)
    ))
  ,

  AdagradOptimizer = _reflection.GeneratedProtocolMessageType('AdagradOptimizer', (_message.Message,), dict(
    DESCRIPTOR = _TPUEMBEDDINGCONFIGURATION_ADAGRADOPTIMIZER,
    __module__ = 'tensorflow.contrib.tpu.proto.tpu_embedding_config_pb2'
    # @@protoc_insertion_point(class_scope:tensorflow.tpu.TPUEmbeddingConfiguration.AdagradOptimizer)
    ))
  ,

  TPUEmbeddingTable = _reflection.GeneratedProtocolMessageType('TPUEmbeddingTable', (_message.Message,), dict(
    DESCRIPTOR = _TPUEMBEDDINGCONFIGURATION_TPUEMBEDDINGTABLE,
    __module__ = 'tensorflow.contrib.tpu.proto.tpu_embedding_config_pb2'
    # @@protoc_insertion_point(class_scope:tensorflow.tpu.TPUEmbeddingConfiguration.TPUEmbeddingTable)
    ))
  ,
  DESCRIPTOR = _TPUEMBEDDINGCONFIGURATION,
  __module__ = 'tensorflow.contrib.tpu.proto.tpu_embedding_config_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.tpu.TPUEmbeddingConfiguration)
  ))
_sym_db.RegisterMessage(TPUEmbeddingConfiguration)
_sym_db.RegisterMessage(TPUEmbeddingConfiguration.GradientDescentOptimizer)
_sym_db.RegisterMessage(TPUEmbeddingConfiguration.AdagradOptimizer)
_sym_db.RegisterMessage(TPUEmbeddingConfiguration.TPUEmbeddingTable)


# @@protoc_insertion_point(module_scope)