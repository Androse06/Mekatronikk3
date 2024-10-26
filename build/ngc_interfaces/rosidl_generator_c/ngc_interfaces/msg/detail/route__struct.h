// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from ngc_interfaces:msg/Route.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "ngc_interfaces/msg/route.h"


#ifndef NGC_INTERFACES__MSG__DETAIL__ROUTE__STRUCT_H_
#define NGC_INTERFACES__MSG__DETAIL__ROUTE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

// Constants defined in the message

// Include directives for member types
// Member 'route_name'
#include "rosidl_runtime_c/string.h"
// Member 'waypoints'
#include "ngc_interfaces/msg/detail/waypoint__struct.h"

/// Struct defined in msg/Route in the package ngc_interfaces.
typedef struct ngc_interfaces__msg__Route
{
  /// Name of the route
  rosidl_runtime_c__String route_name;
  /// List of waypoints
  ngc_interfaces__msg__Waypoint__Sequence waypoints;
} ngc_interfaces__msg__Route;

// Struct for a sequence of ngc_interfaces__msg__Route.
typedef struct ngc_interfaces__msg__Route__Sequence
{
  ngc_interfaces__msg__Route * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} ngc_interfaces__msg__Route__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // NGC_INTERFACES__MSG__DETAIL__ROUTE__STRUCT_H_
