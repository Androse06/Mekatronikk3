// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from ngc_interfaces:msg/Route.idl
// generated code does not contain a copyright notice
#include "ngc_interfaces/msg/detail/route__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <cstddef>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/serialization_helpers.hpp"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "ngc_interfaces/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "ngc_interfaces/msg/detail/route__struct.h"
#include "ngc_interfaces/msg/detail/route__functions.h"
#include "fastcdr/Cdr.h"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

// includes and forward declarations of message dependencies and their conversion functions

#if defined(__cplusplus)
extern "C"
{
#endif

#include "ngc_interfaces/msg/detail/waypoint__functions.h"  // waypoints
#include "rosidl_runtime_c/string.h"  // route_name
#include "rosidl_runtime_c/string_functions.h"  // route_name

// forward declare type support functions

bool cdr_serialize_ngc_interfaces__msg__Waypoint(
  const ngc_interfaces__msg__Waypoint * ros_message,
  eprosima::fastcdr::Cdr & cdr);

bool cdr_deserialize_ngc_interfaces__msg__Waypoint(
  eprosima::fastcdr::Cdr & cdr,
  ngc_interfaces__msg__Waypoint * ros_message);

size_t get_serialized_size_ngc_interfaces__msg__Waypoint(
  const void * untyped_ros_message,
  size_t current_alignment);

size_t max_serialized_size_ngc_interfaces__msg__Waypoint(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

bool cdr_serialize_key_ngc_interfaces__msg__Waypoint(
  const ngc_interfaces__msg__Waypoint * ros_message,
  eprosima::fastcdr::Cdr & cdr);

size_t get_serialized_size_key_ngc_interfaces__msg__Waypoint(
  const void * untyped_ros_message,
  size_t current_alignment);

size_t max_serialized_size_key_ngc_interfaces__msg__Waypoint(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

const rosidl_message_type_support_t *
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, ngc_interfaces, msg, Waypoint)();


using _Route__ros_msg_type = ngc_interfaces__msg__Route;


ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_ngc_interfaces
bool cdr_serialize_ngc_interfaces__msg__Route(
  const ngc_interfaces__msg__Route * ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  // Field name: route_name
  {
    const rosidl_runtime_c__String * str = &ros_message->route_name;
    if (str->capacity == 0 || str->capacity <= str->size) {
      fprintf(stderr, "string capacity not greater than size\n");
      return false;
    }
    if (str->data[str->size] != '\0') {
      fprintf(stderr, "string not null-terminated\n");
      return false;
    }
    cdr << str->data;
  }

  // Field name: waypoints
  {
    size_t size = ros_message->waypoints.size;
    auto array_ptr = ros_message->waypoints.data;
    cdr << static_cast<uint32_t>(size);
    for (size_t i = 0; i < size; ++i) {
      cdr_serialize_ngc_interfaces__msg__Waypoint(
        &array_ptr[i], cdr);
    }
  }

  return true;
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_ngc_interfaces
bool cdr_deserialize_ngc_interfaces__msg__Route(
  eprosima::fastcdr::Cdr & cdr,
  ngc_interfaces__msg__Route * ros_message)
{
  // Field name: route_name
  {
    std::string tmp;
    cdr >> tmp;
    if (!ros_message->route_name.data) {
      rosidl_runtime_c__String__init(&ros_message->route_name);
    }
    bool succeeded = rosidl_runtime_c__String__assign(
      &ros_message->route_name,
      tmp.c_str());
    if (!succeeded) {
      fprintf(stderr, "failed to assign string into field 'route_name'\n");
      return false;
    }
  }

  // Field name: waypoints
  {
    uint32_t cdrSize;
    cdr >> cdrSize;
    size_t size = static_cast<size_t>(cdrSize);
    if (ros_message->waypoints.data) {
      ngc_interfaces__msg__Waypoint__Sequence__fini(&ros_message->waypoints);
    }
    if (!ngc_interfaces__msg__Waypoint__Sequence__init(&ros_message->waypoints, size)) {
      fprintf(stderr, "failed to create array for field 'waypoints'");
      return false;
    }
    auto array_ptr = ros_message->waypoints.data;
    for (size_t i = 0; i < size; ++i) {
      cdr_deserialize_ngc_interfaces__msg__Waypoint(cdr, &array_ptr[i]);
    }
  }

  return true;
}  // NOLINT(readability/fn_size)


ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_ngc_interfaces
size_t get_serialized_size_ngc_interfaces__msg__Route(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _Route__ros_msg_type * ros_message = static_cast<const _Route__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // Field name: route_name
  current_alignment += padding +
    eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
    (ros_message->route_name.size + 1);

  // Field name: waypoints
  {
    size_t array_size = ros_message->waypoints.size;
    auto array_ptr = ros_message->waypoints.data;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);
    for (size_t index = 0; index < array_size; ++index) {
      current_alignment += get_serialized_size_ngc_interfaces__msg__Waypoint(
        &array_ptr[index], current_alignment);
    }
  }

  return current_alignment - initial_alignment;
}


ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_ngc_interfaces
size_t max_serialized_size_ngc_interfaces__msg__Route(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  size_t last_member_size = 0;
  (void)last_member_size;
  (void)padding;
  (void)wchar_size;

  full_bounded = true;
  is_plain = true;

  // Field name: route_name
  {
    size_t array_size = 1;
    full_bounded = false;
    is_plain = false;
    for (size_t index = 0; index < array_size; ++index) {
      current_alignment += padding +
        eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
        1;
    }
  }

  // Field name: waypoints
  {
    size_t array_size = 0;
    full_bounded = false;
    is_plain = false;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);
    last_member_size = 0;
    for (size_t index = 0; index < array_size; ++index) {
      bool inner_full_bounded;
      bool inner_is_plain;
      size_t inner_size;
      inner_size =
        max_serialized_size_ngc_interfaces__msg__Waypoint(
        inner_full_bounded, inner_is_plain, current_alignment);
      last_member_size += inner_size;
      current_alignment += inner_size;
      full_bounded &= inner_full_bounded;
      is_plain &= inner_is_plain;
    }
  }


  size_t ret_val = current_alignment - initial_alignment;
  if (is_plain) {
    // All members are plain, and type is not empty.
    // We still need to check that the in-memory alignment
    // is the same as the CDR mandated alignment.
    using DataType = ngc_interfaces__msg__Route;
    is_plain =
      (
      offsetof(DataType, waypoints) +
      last_member_size
      ) == ret_val;
  }
  return ret_val;
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_ngc_interfaces
bool cdr_serialize_key_ngc_interfaces__msg__Route(
  const ngc_interfaces__msg__Route * ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  // Field name: route_name
  {
    const rosidl_runtime_c__String * str = &ros_message->route_name;
    if (str->capacity == 0 || str->capacity <= str->size) {
      fprintf(stderr, "string capacity not greater than size\n");
      return false;
    }
    if (str->data[str->size] != '\0') {
      fprintf(stderr, "string not null-terminated\n");
      return false;
    }
    cdr << str->data;
  }

  // Field name: waypoints
  {
    size_t size = ros_message->waypoints.size;
    auto array_ptr = ros_message->waypoints.data;
    cdr << static_cast<uint32_t>(size);
    for (size_t i = 0; i < size; ++i) {
      cdr_serialize_key_ngc_interfaces__msg__Waypoint(
        &array_ptr[i], cdr);
    }
  }

  return true;
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_ngc_interfaces
size_t get_serialized_size_key_ngc_interfaces__msg__Route(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _Route__ros_msg_type * ros_message = static_cast<const _Route__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;

  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // Field name: route_name
  current_alignment += padding +
    eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
    (ros_message->route_name.size + 1);

  // Field name: waypoints
  {
    size_t array_size = ros_message->waypoints.size;
    auto array_ptr = ros_message->waypoints.data;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);
    for (size_t index = 0; index < array_size; ++index) {
      current_alignment += get_serialized_size_key_ngc_interfaces__msg__Waypoint(
        &array_ptr[index], current_alignment);
    }
  }

  return current_alignment - initial_alignment;
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_ngc_interfaces
size_t max_serialized_size_key_ngc_interfaces__msg__Route(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  size_t last_member_size = 0;
  (void)last_member_size;
  (void)padding;
  (void)wchar_size;

  full_bounded = true;
  is_plain = true;
  // Field name: route_name
  {
    size_t array_size = 1;
    full_bounded = false;
    is_plain = false;
    for (size_t index = 0; index < array_size; ++index) {
      current_alignment += padding +
        eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
        1;
    }
  }

  // Field name: waypoints
  {
    size_t array_size = 0;
    full_bounded = false;
    is_plain = false;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);
    last_member_size = 0;
    for (size_t index = 0; index < array_size; ++index) {
      bool inner_full_bounded;
      bool inner_is_plain;
      size_t inner_size;
      inner_size =
        max_serialized_size_key_ngc_interfaces__msg__Waypoint(
        inner_full_bounded, inner_is_plain, current_alignment);
      last_member_size += inner_size;
      current_alignment += inner_size;
      full_bounded &= inner_full_bounded;
      is_plain &= inner_is_plain;
    }
  }

  size_t ret_val = current_alignment - initial_alignment;
  if (is_plain) {
    // All members are plain, and type is not empty.
    // We still need to check that the in-memory alignment
    // is the same as the CDR mandated alignment.
    using DataType = ngc_interfaces__msg__Route;
    is_plain =
      (
      offsetof(DataType, waypoints) +
      last_member_size
      ) == ret_val;
  }
  return ret_val;
}


static bool _Route__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const ngc_interfaces__msg__Route * ros_message = static_cast<const ngc_interfaces__msg__Route *>(untyped_ros_message);
  (void)ros_message;
  return cdr_serialize_ngc_interfaces__msg__Route(ros_message, cdr);
}

static bool _Route__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  ngc_interfaces__msg__Route * ros_message = static_cast<ngc_interfaces__msg__Route *>(untyped_ros_message);
  (void)ros_message;
  return cdr_deserialize_ngc_interfaces__msg__Route(cdr, ros_message);
}

static uint32_t _Route__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_ngc_interfaces__msg__Route(
      untyped_ros_message, 0));
}

static size_t _Route__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_ngc_interfaces__msg__Route(
    full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}


static message_type_support_callbacks_t __callbacks_Route = {
  "ngc_interfaces::msg",
  "Route",
  _Route__cdr_serialize,
  _Route__cdr_deserialize,
  _Route__get_serialized_size,
  _Route__max_serialized_size,
  nullptr
};

static rosidl_message_type_support_t _Route__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_Route,
  get_message_typesupport_handle_function,
  &ngc_interfaces__msg__Route__get_type_hash,
  &ngc_interfaces__msg__Route__get_type_description,
  &ngc_interfaces__msg__Route__get_type_description_sources,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, ngc_interfaces, msg, Route)() {
  return &_Route__type_support;
}

#if defined(__cplusplus)
}
#endif
