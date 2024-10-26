// generated from rosidl_generator_c/resource/idl__description.c.em
// with input from ngc_interfaces:msg/Route.idl
// generated code does not contain a copyright notice

#include "ngc_interfaces/msg/detail/route__functions.h"

ROSIDL_GENERATOR_C_PUBLIC_ngc_interfaces
const rosidl_type_hash_t *
ngc_interfaces__msg__Route__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0x57, 0xda, 0xe0, 0x48, 0x07, 0x87, 0x55, 0xc7,
      0x12, 0x8b, 0xbd, 0x21, 0x06, 0x83, 0xdc, 0x38,
      0x67, 0x0d, 0xe2, 0x0d, 0xa9, 0xce, 0x12, 0xbe,
      0xd2, 0x46, 0x69, 0x6c, 0xc1, 0x5d, 0x4a, 0xad,
    }};
  return &hash;
}

#include <assert.h>
#include <string.h>

// Include directives for referenced types
#include "ngc_interfaces/msg/detail/waypoint__functions.h"

// Hashes for external referenced types
#ifndef NDEBUG
static const rosidl_type_hash_t ngc_interfaces__msg__Waypoint__EXPECTED_HASH = {1, {
    0x9e, 0x6a, 0x63, 0x0e, 0x15, 0x5e, 0x6a, 0x0d,
    0xce, 0xfe, 0x21, 0xfe, 0x88, 0x7e, 0x7b, 0xf6,
    0x55, 0x46, 0x18, 0xce, 0x95, 0x13, 0x7e, 0x56,
    0xfd, 0x77, 0x6d, 0xca, 0x04, 0x29, 0x85, 0x9e,
  }};
#endif

static char ngc_interfaces__msg__Route__TYPE_NAME[] = "ngc_interfaces/msg/Route";
static char ngc_interfaces__msg__Waypoint__TYPE_NAME[] = "ngc_interfaces/msg/Waypoint";

// Define type names, field names, and default values
static char ngc_interfaces__msg__Route__FIELD_NAME__route_name[] = "route_name";
static char ngc_interfaces__msg__Route__FIELD_NAME__waypoints[] = "waypoints";

static rosidl_runtime_c__type_description__Field ngc_interfaces__msg__Route__FIELDS[] = {
  {
    {ngc_interfaces__msg__Route__FIELD_NAME__route_name, 10, 10},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_STRING,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {ngc_interfaces__msg__Route__FIELD_NAME__waypoints, 9, 9},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE_UNBOUNDED_SEQUENCE,
      0,
      0,
      {ngc_interfaces__msg__Waypoint__TYPE_NAME, 27, 27},
    },
    {NULL, 0, 0},
  },
};

static rosidl_runtime_c__type_description__IndividualTypeDescription ngc_interfaces__msg__Route__REFERENCED_TYPE_DESCRIPTIONS[] = {
  {
    {ngc_interfaces__msg__Waypoint__TYPE_NAME, 27, 27},
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
ngc_interfaces__msg__Route__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {ngc_interfaces__msg__Route__TYPE_NAME, 24, 24},
      {ngc_interfaces__msg__Route__FIELDS, 2, 2},
    },
    {ngc_interfaces__msg__Route__REFERENCED_TYPE_DESCRIPTIONS, 1, 1},
  };
  if (!constructed) {
    assert(0 == memcmp(&ngc_interfaces__msg__Waypoint__EXPECTED_HASH, ngc_interfaces__msg__Waypoint__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[0].fields = ngc_interfaces__msg__Waypoint__get_type_description(NULL)->type_description.fields;
    constructed = true;
  }
  return &description;
}

static char toplevel_type_raw_source[] =
  "string route_name      # Name of the route\n"
  "Waypoint[] waypoints   # List of waypoints";

static char msg_encoding[] = "msg";

// Define all individual source functions

const rosidl_runtime_c__type_description__TypeSource *
ngc_interfaces__msg__Route__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {ngc_interfaces__msg__Route__TYPE_NAME, 24, 24},
    {msg_encoding, 3, 3},
    {toplevel_type_raw_source, 85, 85},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
ngc_interfaces__msg__Route__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[2];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 2, 2};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *ngc_interfaces__msg__Route__get_individual_type_description_source(NULL),
    sources[1] = *ngc_interfaces__msg__Waypoint__get_individual_type_description_source(NULL);
    constructed = true;
  }
  return &source_sequence;
}
