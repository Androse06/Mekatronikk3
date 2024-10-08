// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from ngc_interfaces:msg/HeadingDevice.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "ngc_interfaces/msg/heading_device.h"


#ifndef NGC_INTERFACES__MSG__DETAIL__HEADING_DEVICE__STRUCT_H_
#define NGC_INTERFACES__MSG__DETAIL__HEADING_DEVICE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

// Constants defined in the message

/// Struct defined in msg/HeadingDevice in the package ngc_interfaces.
/**
  * A heading device (gyro, gnss, compass) output 
 */
typedef struct ngc_interfaces__msg__HeadingDevice
{
  /// in radians
  float heading;
  /// in radians pr. sec
  float rot;
  bool valid_signal;
  int32_t id;
} ngc_interfaces__msg__HeadingDevice;

// Struct for a sequence of ngc_interfaces__msg__HeadingDevice.
typedef struct ngc_interfaces__msg__HeadingDevice__Sequence
{
  ngc_interfaces__msg__HeadingDevice * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} ngc_interfaces__msg__HeadingDevice__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // NGC_INTERFACES__MSG__DETAIL__HEADING_DEVICE__STRUCT_H_
