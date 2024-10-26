// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from ngc_interfaces:msg/HMI.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "ngc_interfaces/msg/hmi.h"


#ifndef NGC_INTERFACES__MSG__DETAIL__HMI__STRUCT_H_
#define NGC_INTERFACES__MSG__DETAIL__HMI__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

// Constants defined in the message

/// Struct defined in msg/HMI in the package ngc_interfaces.
typedef struct ngc_interfaces__msg__HMI
{
  /// Alle kontrollfunksjoner
  int32_t mode;
  /// Loader waypoints for track
  bool route;
  /// Loader waypoint for DP
  bool point;
  float nu;
  float eta;
} ngc_interfaces__msg__HMI;

// Struct for a sequence of ngc_interfaces__msg__HMI.
typedef struct ngc_interfaces__msg__HMI__Sequence
{
  ngc_interfaces__msg__HMI * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} ngc_interfaces__msg__HMI__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // NGC_INTERFACES__MSG__DETAIL__HMI__STRUCT_H_
