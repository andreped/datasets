# coding=utf-8
# Copyright 2023 The TensorFlow Datasets Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# pylint: skip-file

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow_datasets/proto/tf_feature.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n*tensorflow_datasets/proto/tf_feature.proto\x12\x0ftensorflow_copy"\x1a\n\tBytesList\x12\r\n\x05value\x18\x01'
    b' \x03(\x0c"\x1e\n\tFloatList\x12\x11\n\x05value\x18\x01'
    b' \x03(\x02\x42\x02\x10\x01"\x1e\n\tInt64List\x12\x11\n\x05value\x18\x01'
    b' \x03(\x03\x42\x02\x10\x01"\xa7\x01\n\x07\x46\x65\x61ture\x12\x30\n\nbytes_list\x18\x01'
    b' \x01(\x0b\x32\x1a.tensorflow_copy.BytesListH\x00\x12\x30\n\nfloat_list\x18\x02'
    b' \x01(\x0b\x32\x1a.tensorflow_copy.FloatListH\x00\x12\x30\n\nint64_list\x18\x03'
    b' \x01(\x0b\x32\x1a.tensorflow_copy.Int64ListH\x00\x42\x06\n\x04kind"\x8d\x01\n\x08\x46\x65\x61tures\x12\x37\n\x07\x66\x65\x61ture\x18\x01'
    b' \x03(\x0b\x32&.tensorflow_copy.Features.FeatureEntry\x1aH\n\x0c\x46\x65\x61tureEntry\x12\x0b\n\x03key\x18\x01'
    b" \x01(\t\x12'\n\x05value\x18\x02"
    b' \x01(\x0b\x32\x18.tensorflow_copy.Feature:\x02\x38\x01"8\n\x0b\x46\x65\x61tureList\x12)\n\x07\x66\x65\x61ture\x18\x01'
    b' \x03(\x0b\x32\x18.tensorflow_copy.Feature"\xa6\x01\n\x0c\x46\x65\x61tureLists\x12\x44\n\x0c\x66\x65\x61ture_list\x18\x01'
    b' \x03(\x0b\x32..tensorflow_copy.FeatureLists.FeatureListEntry\x1aP\n\x10\x46\x65\x61tureListEntry\x12\x0b\n\x03key\x18\x01'
    b' \x01(\t\x12+\n\x05value\x18\x02'
    b' \x01(\x0b\x32\x1c.tensorflow_copy.FeatureList:\x02\x38\x01\x42\x81\x01\n\x16org.tensorflow.exampleB\rFeatureProtosP\x01ZSgithub.com/tensorflow/tensorflow/tensorflow/go/core/example/example_protos_go_proto\xf8\x01\x01\x62\x06proto3'
)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, 'tensorflow_datasets.proto.tf_feature_pb2', globals()
)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\026org.tensorflow.exampleB\rFeatureProtosP\001ZSgithub.com/tensorflow/tensorflow/tensorflow/go/core/example/example_protos_go_proto\370\001\001'
  _FLOATLIST.fields_by_name['value']._options = None
  _FLOATLIST.fields_by_name['value']._serialized_options = b'\020\001'
  _INT64LIST.fields_by_name['value']._options = None
  _INT64LIST.fields_by_name['value']._serialized_options = b'\020\001'
  _FEATURES_FEATUREENTRY._options = None
  _FEATURES_FEATUREENTRY._serialized_options = b'8\001'
  _FEATURELISTS_FEATURELISTENTRY._options = None
  _FEATURELISTS_FEATURELISTENTRY._serialized_options = b'8\001'
  _BYTESLIST._serialized_start = 63
  _BYTESLIST._serialized_end = 89
  _FLOATLIST._serialized_start = 91
  _FLOATLIST._serialized_end = 121
  _INT64LIST._serialized_start = 123
  _INT64LIST._serialized_end = 153
  _FEATURE._serialized_start = 156
  _FEATURE._serialized_end = 323
  _FEATURES._serialized_start = 326
  _FEATURES._serialized_end = 467
  _FEATURES_FEATUREENTRY._serialized_start = 395
  _FEATURES_FEATUREENTRY._serialized_end = 467
  _FEATURELIST._serialized_start = 469
  _FEATURELIST._serialized_end = 525
  _FEATURELISTS._serialized_start = 528
  _FEATURELISTS._serialized_end = 694
  _FEATURELISTS_FEATURELISTENTRY._serialized_start = 614
  _FEATURELISTS_FEATURELISTENTRY._serialized_end = 694
# @@protoc_insertion_point(module_scope)
