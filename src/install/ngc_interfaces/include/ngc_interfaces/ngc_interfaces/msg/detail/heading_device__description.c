// generated from rosidl_generator_c/resource/idl__description.c.em
// with input from ngc_interfaces:msg/HeadingDevice.idl
// generated code does not contain a copyright notice

#include "ngc_interfaces/msg/detail/heading_device__functions.h"

ROSIDL_GENERATOR_C_PUBLIC_ngc_interfaces
const rosidl_type_hash_t *
ngc_interfaces__msg__HeadingDevice__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0x0e, 0x83, 0x57, 0xb1, 0xde, 0x55, 0xcf, 0xca,
      0x51, 0x27, 0x6b, 0x36, 0xb9, 0x2c, 0x24, 0x74,
      0x15, 0x5e, 0x61, 0xcb, 0x18, 0x99, 0x03, 0x86,
      0x91, 0x3b, 0x9b, 0xe6, 0xb3, 0x21, 0x3c, 0x9d,
    }};
  return &hash;
}

#include <assert.h>
#include <string.h>

// Include directives for referenced types

// Hashes for external referenced types
#ifndef NDEBUG
#endif

static char ngc_interfaces__msg__HeadingDevice__TYPE_NAME[] = "ngc_interfaces/msg/HeadingDevice";

// Define type names, field names, and default values
static char ngc_interfaces__msg__HeadingDevice__FIELD_NAME__heading[] = "heading";
static char ngc_interfaces__msg__HeadingDevice__FIELD_NAME__rot[] = "rot";
static char ngc_interfaces__msg__HeadingDevice__FIELD_NAME__valid_signal[] = "valid_signal";
static char ngc_interfaces__msg__HeadingDevice__FIELD_NAME__id[] = "id";

static rosidl_runtime_c__type_description__Field ngc_interfaces__msg__HeadingDevice__FIELDS[] = {
  {
    {ngc_interfaces__msg__HeadingDevice__FIELD_NAME__heading, 7, 7},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {ngc_interfaces__msg__HeadingDevice__FIELD_NAME__rot, 3, 3},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {ngc_interfaces__msg__HeadingDevice__FIELD_NAME__valid_signal, 12, 12},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_BOOLEAN,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {ngc_interfaces__msg__HeadingDevice__FIELD_NAME__id, 2, 2},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_INT32,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
ngc_interfaces__msg__HeadingDevice__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {ngc_interfaces__msg__HeadingDevice__TYPE_NAME, 32, 32},
      {ngc_interfaces__msg__HeadingDevice__FIELDS, 4, 4},
    },
    {NULL, 0, 0},
  };
  if (!constructed) {
    constructed = true;
  }
  return &description;
}

static char toplevel_type_raw_source[] =
  "# A heading device (gyro, gnss, compass) output \n"
  "float32 heading             # in radians \n"
  "float32 rot                 # in radians pr. sec\n"
  "bool    valid_signal\n"
  "int32   id";

static char msg_encoding[] = "msg";

// Define all individual source functions

const rosidl_runtime_c__type_description__TypeSource *
ngc_interfaces__msg__HeadingDevice__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {ngc_interfaces__msg__HeadingDevice__TYPE_NAME, 32, 32},
    {msg_encoding, 3, 3},
    {toplevel_type_raw_source, 171, 171},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
ngc_interfaces__msg__HeadingDevice__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[1];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 1, 1};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *ngc_interfaces__msg__HeadingDevice__get_individual_type_description_source(NULL),
    constructed = true;
  }
  return &source_sequence;
}
