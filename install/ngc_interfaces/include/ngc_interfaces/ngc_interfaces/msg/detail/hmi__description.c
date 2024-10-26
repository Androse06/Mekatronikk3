// generated from rosidl_generator_c/resource/idl__description.c.em
// with input from ngc_interfaces:msg/HMI.idl
// generated code does not contain a copyright notice

#include "ngc_interfaces/msg/detail/hmi__functions.h"

ROSIDL_GENERATOR_C_PUBLIC_ngc_interfaces
const rosidl_type_hash_t *
ngc_interfaces__msg__HMI__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0xf1, 0xcc, 0x0a, 0x84, 0x50, 0xfd, 0xd0, 0x33,
      0x4c, 0x9a, 0x64, 0x8d, 0xec, 0x92, 0x74, 0xe2,
      0xed, 0x82, 0x33, 0x9e, 0x8f, 0x76, 0xd5, 0x93,
      0xe0, 0xb5, 0xc0, 0xd3, 0xa6, 0x86, 0x81, 0x58,
    }};
  return &hash;
}

#include <assert.h>
#include <string.h>

// Include directives for referenced types

// Hashes for external referenced types
#ifndef NDEBUG
#endif

static char ngc_interfaces__msg__HMI__TYPE_NAME[] = "ngc_interfaces/msg/HMI";

// Define type names, field names, and default values
static char ngc_interfaces__msg__HMI__FIELD_NAME__mode[] = "mode";
static char ngc_interfaces__msg__HMI__FIELD_NAME__route[] = "route";
static char ngc_interfaces__msg__HMI__FIELD_NAME__point[] = "point";
static char ngc_interfaces__msg__HMI__FIELD_NAME__nu[] = "nu";
static char ngc_interfaces__msg__HMI__FIELD_NAME__eta[] = "eta";

static rosidl_runtime_c__type_description__Field ngc_interfaces__msg__HMI__FIELDS[] = {
  {
    {ngc_interfaces__msg__HMI__FIELD_NAME__mode, 4, 4},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_INT32,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {ngc_interfaces__msg__HMI__FIELD_NAME__route, 5, 5},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_BOOLEAN,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {ngc_interfaces__msg__HMI__FIELD_NAME__point, 5, 5},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_BOOLEAN,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {ngc_interfaces__msg__HMI__FIELD_NAME__nu, 2, 2},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {ngc_interfaces__msg__HMI__FIELD_NAME__eta, 3, 3},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
ngc_interfaces__msg__HMI__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {ngc_interfaces__msg__HMI__TYPE_NAME, 22, 22},
      {ngc_interfaces__msg__HMI__FIELDS, 5, 5},
    },
    {NULL, 0, 0},
  };
  if (!constructed) {
    constructed = true;
  }
  return &description;
}

static char toplevel_type_raw_source[] =
  "int32 mode      # Alle kontrollfunksjoner\n"
  "bool route      # Loader waypoints for track\n"
  "bool point      # Loader waypoint for DP\n"
  "float32 nu\n"
  "float32 eta";

static char msg_encoding[] = "msg";

// Define all individual source functions

const rosidl_runtime_c__type_description__TypeSource *
ngc_interfaces__msg__HMI__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {ngc_interfaces__msg__HMI__TYPE_NAME, 22, 22},
    {msg_encoding, 3, 3},
    {toplevel_type_raw_source, 150, 150},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
ngc_interfaces__msg__HMI__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[1];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 1, 1};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *ngc_interfaces__msg__HMI__get_individual_type_description_source(NULL),
    constructed = true;
  }
  return &source_sequence;
}
