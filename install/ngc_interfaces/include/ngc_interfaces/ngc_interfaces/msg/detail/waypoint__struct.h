// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from ngc_interfaces:msg/Waypoint.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "ngc_interfaces/msg/waypoint.h"


#ifndef NGC_INTERFACES__MSG__DETAIL__WAYPOINT__STRUCT_H_
#define NGC_INTERFACES__MSG__DETAIL__WAYPOINT__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

// Constants defined in the message

// Include directives for member types
// Member 'name'
#include "rosidl_runtime_c/string.h"

/// Struct defined in msg/Waypoint in the package ngc_interfaces.
typedef struct ngc_interfaces__msg__Waypoint
{
  /// Latitude of the waypoint
  double latitude;
  /// Longitude of the waypoint
  double longitude;
  /// Name of the waypoint
  rosidl_runtime_c__String name;
} ngc_interfaces__msg__Waypoint;

// Struct for a sequence of ngc_interfaces__msg__Waypoint.
typedef struct ngc_interfaces__msg__Waypoint__Sequence
{
  ngc_interfaces__msg__Waypoint * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} ngc_interfaces__msg__Waypoint__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // NGC_INTERFACES__MSG__DETAIL__WAYPOINT__STRUCT_H_
