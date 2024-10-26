// generated from rosidl_generator_c/resource/idl__description.c.em
// with input from ngc_interfaces:msg/Waypoint.idl
// generated code does not contain a copyright notice

#include "ngc_interfaces/msg/detail/waypoint__functions.h"

ROSIDL_GENERATOR_C_PUBLIC_ngc_interfaces
const rosidl_type_hash_t *
ngc_interfaces__msg__Waypoint__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0x9e, 0x6a, 0x63, 0x0e, 0x15, 0x5e, 0x6a, 0x0d,
      0xce, 0xfe, 0x21, 0xfe, 0x88, 0x7e, 0x7b, 0xf6,
      0x55, 0x46, 0x18, 0xce, 0x95, 0x13, 0x7e, 0x56,
      0xfd, 0x77, 0x6d, 0xca, 0x04, 0x29, 0x85, 0x9e,
    }};
  return &hash;
}

#include <assert.h>
#include <string.h>

// Include directives for referenced types

// Hashes for external referenced types
#ifndef NDEBUG
#endif

static char ngc_interfaces__msg__Waypoint__TYPE_NAME[] = "ngc_interfaces/msg/Waypoint";

// Define type names, field names, and default values
static char ngc_interfaces__msg__Waypoint__FIELD_NAME__latitude[] = "latitude";
static char ngc_interfaces__msg__Waypoint__FIELD_NAME__longitude[] = "longitude";
static char ngc_interfaces__msg__Waypoint__FIELD_NAME__name[] = "name";

static rosidl_runtime_c__type_description__Field ngc_interfaces__msg__Waypoint__FIELDS[] = {
  {
    {ngc_interfaces__msg__Waypoint__FIELD_NAME__latitude, 8, 8},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {ngc_interfaces__msg__Waypoint__FIELD_NAME__longitude, 9, 9},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {ngc_interfaces__msg__Waypoint__FIELD_NAME__name, 4, 4},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_STRING,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
ngc_interfaces__msg__Waypoint__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {ngc_interfaces__msg__Waypoint__TYPE_NAME, 27, 27},
      {ngc_interfaces__msg__Waypoint__FIELDS, 3, 3},
    },
    {NULL, 0, 0},
  };
  if (!constructed) {
    constructed = true;
  }
  return &description;
}

static char toplevel_type_raw_source[] =
  "float64 latitude      # Latitude of the waypoint\n"
  "float64 longitude     # Longitude of the waypoint\n"
  "string name           # Name of the waypoint";

static char msg_encoding[] = "msg";

// Define all individual source functions

const rosidl_runtime_c__type_description__TypeSource *
ngc_interfaces__msg__Waypoint__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {ngc_interfaces__msg__Waypoint__TYPE_NAME, 27, 27},
    {msg_encoding, 3, 3},
    {toplevel_type_raw_source, 143, 143},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
ngc_interfaces__msg__Waypoint__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[1];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 1, 1};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *ngc_interfaces__msg__Waypoint__get_individual_type_description_source(NULL),
    constructed = true;
  }
  return &source_sequence;
}
