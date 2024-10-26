// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from ngc_interfaces:msg/Route.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "ngc_interfaces/msg/detail/route__rosidl_typesupport_introspection_c.h"
#include "ngc_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "ngc_interfaces/msg/detail/route__functions.h"
#include "ngc_interfaces/msg/detail/route__struct.h"


// Include directives for member types
// Member `route_name`
#include "rosidl_runtime_c/string_functions.h"
// Member `waypoints`
#include "ngc_interfaces/msg/waypoint.h"
// Member `waypoints`
#include "ngc_interfaces/msg/detail/waypoint__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void ngc_interfaces__msg__Route__rosidl_typesupport_introspection_c__Route_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  ngc_interfaces__msg__Route__init(message_memory);
}

void ngc_interfaces__msg__Route__rosidl_typesupport_introspection_c__Route_fini_function(void * message_memory)
{
  ngc_interfaces__msg__Route__fini(message_memory);
}

size_t ngc_interfaces__msg__Route__rosidl_typesupport_introspection_c__size_function__Route__waypoints(
  const void * untyped_member)
{
  const ngc_interfaces__msg__Waypoint__Sequence * member =
    (const ngc_interfaces__msg__Waypoint__Sequence *)(untyped_member);
  return member->size;
}

const void * ngc_interfaces__msg__Route__rosidl_typesupport_introspection_c__get_const_function__Route__waypoints(
  const void * untyped_member, size_t index)
{
  const ngc_interfaces__msg__Waypoint__Sequence * member =
    (const ngc_interfaces__msg__Waypoint__Sequence *)(untyped_member);
  return &member->data[index];
}

void * ngc_interfaces__msg__Route__rosidl_typesupport_introspection_c__get_function__Route__waypoints(
  void * untyped_member, size_t index)
{
  ngc_interfaces__msg__Waypoint__Sequence * member =
    (ngc_interfaces__msg__Waypoint__Sequence *)(untyped_member);
  return &member->data[index];
}

void ngc_interfaces__msg__Route__rosidl_typesupport_introspection_c__fetch_function__Route__waypoints(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const ngc_interfaces__msg__Waypoint * item =
    ((const ngc_interfaces__msg__Waypoint *)
    ngc_interfaces__msg__Route__rosidl_typesupport_introspection_c__get_const_function__Route__waypoints(untyped_member, index));
  ngc_interfaces__msg__Waypoint * value =
    (ngc_interfaces__msg__Waypoint *)(untyped_value);
  *value = *item;
}

void ngc_interfaces__msg__Route__rosidl_typesupport_introspection_c__assign_function__Route__waypoints(
  void * untyped_member, size_t index, const void * untyped_value)
{
  ngc_interfaces__msg__Waypoint * item =
    ((ngc_interfaces__msg__Waypoint *)
    ngc_interfaces__msg__Route__rosidl_typesupport_introspection_c__get_function__Route__waypoints(untyped_member, index));
  const ngc_interfaces__msg__Waypoint * value =
    (const ngc_interfaces__msg__Waypoint *)(untyped_value);
  *item = *value;
}

bool ngc_interfaces__msg__Route__rosidl_typesupport_introspection_c__resize_function__Route__waypoints(
  void * untyped_member, size_t size)
{
  ngc_interfaces__msg__Waypoint__Sequence * member =
    (ngc_interfaces__msg__Waypoint__Sequence *)(untyped_member);
  ngc_interfaces__msg__Waypoint__Sequence__fini(member);
  return ngc_interfaces__msg__Waypoint__Sequence__init(member, size);
}

static rosidl_typesupport_introspection_c__MessageMember ngc_interfaces__msg__Route__rosidl_typesupport_introspection_c__Route_message_member_array[2] = {
  {
    "route_name",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ngc_interfaces__msg__Route, route_name),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "waypoints",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is key
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ngc_interfaces__msg__Route, waypoints),  // bytes offset in struct
    NULL,  // default value
    ngc_interfaces__msg__Route__rosidl_typesupport_introspection_c__size_function__Route__waypoints,  // size() function pointer
    ngc_interfaces__msg__Route__rosidl_typesupport_introspection_c__get_const_function__Route__waypoints,  // get_const(index) function pointer
    ngc_interfaces__msg__Route__rosidl_typesupport_introspection_c__get_function__Route__waypoints,  // get(index) function pointer
    ngc_interfaces__msg__Route__rosidl_typesupport_introspection_c__fetch_function__Route__waypoints,  // fetch(index, &value) function pointer
    ngc_interfaces__msg__Route__rosidl_typesupport_introspection_c__assign_function__Route__waypoints,  // assign(index, value) function pointer
    ngc_interfaces__msg__Route__rosidl_typesupport_introspection_c__resize_function__Route__waypoints  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers ngc_interfaces__msg__Route__rosidl_typesupport_introspection_c__Route_message_members = {
  "ngc_interfaces__msg",  // message namespace
  "Route",  // message name
  2,  // number of fields
  sizeof(ngc_interfaces__msg__Route),
  false,  // has_any_key_member_
  ngc_interfaces__msg__Route__rosidl_typesupport_introspection_c__Route_message_member_array,  // message members
  ngc_interfaces__msg__Route__rosidl_typesupport_introspection_c__Route_init_function,  // function to initialize message memory (memory has to be allocated)
  ngc_interfaces__msg__Route__rosidl_typesupport_introspection_c__Route_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t ngc_interfaces__msg__Route__rosidl_typesupport_introspection_c__Route_message_type_support_handle = {
  0,
  &ngc_interfaces__msg__Route__rosidl_typesupport_introspection_c__Route_message_members,
  get_message_typesupport_handle_function,
  &ngc_interfaces__msg__Route__get_type_hash,
  &ngc_interfaces__msg__Route__get_type_description,
  &ngc_interfaces__msg__Route__get_type_description_sources,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_ngc_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, ngc_interfaces, msg, Route)() {
  ngc_interfaces__msg__Route__rosidl_typesupport_introspection_c__Route_message_member_array[1].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, ngc_interfaces, msg, Waypoint)();
  if (!ngc_interfaces__msg__Route__rosidl_typesupport_introspection_c__Route_message_type_support_handle.typesupport_identifier) {
    ngc_interfaces__msg__Route__rosidl_typesupport_introspection_c__Route_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &ngc_interfaces__msg__Route__rosidl_typesupport_introspection_c__Route_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
