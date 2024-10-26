// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from ngc_interfaces:msg/HMI.idl
// generated code does not contain a copyright notice
#include "ngc_interfaces/msg/detail/hmi__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <cstddef>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/serialization_helpers.hpp"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "ngc_interfaces/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "ngc_interfaces/msg/detail/hmi__struct.h"
#include "ngc_interfaces/msg/detail/hmi__functions.h"
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


// forward declare type support functions


using _HMI__ros_msg_type = ngc_interfaces__msg__HMI;


ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_ngc_interfaces
bool cdr_serialize_ngc_interfaces__msg__HMI(
  const ngc_interfaces__msg__HMI * ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  // Field name: mode
  {
    cdr << ros_message->mode;
  }

  // Field name: route
  {
    cdr << (ros_message->route ? true : false);
  }

  // Field name: point
  {
    cdr << (ros_message->point ? true : false);
  }

  // Field name: nu
  {
    cdr << ros_message->nu;
  }

  // Field name: eta
  {
    cdr << ros_message->eta;
  }

  return true;
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_ngc_interfaces
bool cdr_deserialize_ngc_interfaces__msg__HMI(
  eprosima::fastcdr::Cdr & cdr,
  ngc_interfaces__msg__HMI * ros_message)
{
  // Field name: mode
  {
    cdr >> ros_message->mode;
  }

  // Field name: route
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->route = tmp ? true : false;
  }

  // Field name: point
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->point = tmp ? true : false;
  }

  // Field name: nu
  {
    cdr >> ros_message->nu;
  }

  // Field name: eta
  {
    cdr >> ros_message->eta;
  }

  return true;
}  // NOLINT(readability/fn_size)


ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_ngc_interfaces
size_t get_serialized_size_ngc_interfaces__msg__HMI(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _HMI__ros_msg_type * ros_message = static_cast<const _HMI__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // Field name: mode
  {
    size_t item_size = sizeof(ros_message->mode);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  // Field name: route
  {
    size_t item_size = sizeof(ros_message->route);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  // Field name: point
  {
    size_t item_size = sizeof(ros_message->point);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  // Field name: nu
  {
    size_t item_size = sizeof(ros_message->nu);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  // Field name: eta
  {
    size_t item_size = sizeof(ros_message->eta);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}


ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_ngc_interfaces
size_t max_serialized_size_ngc_interfaces__msg__HMI(
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

  // Field name: mode
  {
    size_t array_size = 1;
    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Field name: route
  {
    size_t array_size = 1;
    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }

  // Field name: point
  {
    size_t array_size = 1;
    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }

  // Field name: nu
  {
    size_t array_size = 1;
    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Field name: eta
  {
    size_t array_size = 1;
    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }


  size_t ret_val = current_alignment - initial_alignment;
  if (is_plain) {
    // All members are plain, and type is not empty.
    // We still need to check that the in-memory alignment
    // is the same as the CDR mandated alignment.
    using DataType = ngc_interfaces__msg__HMI;
    is_plain =
      (
      offsetof(DataType, eta) +
      last_member_size
      ) == ret_val;
  }
  return ret_val;
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_ngc_interfaces
bool cdr_serialize_key_ngc_interfaces__msg__HMI(
  const ngc_interfaces__msg__HMI * ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  // Field name: mode
  {
    cdr << ros_message->mode;
  }

  // Field name: route
  {
    cdr << (ros_message->route ? true : false);
  }

  // Field name: point
  {
    cdr << (ros_message->point ? true : false);
  }

  // Field name: nu
  {
    cdr << ros_message->nu;
  }

  // Field name: eta
  {
    cdr << ros_message->eta;
  }

  return true;
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_ngc_interfaces
size_t get_serialized_size_key_ngc_interfaces__msg__HMI(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _HMI__ros_msg_type * ros_message = static_cast<const _HMI__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;

  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // Field name: mode
  {
    size_t item_size = sizeof(ros_message->mode);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  // Field name: route
  {
    size_t item_size = sizeof(ros_message->route);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  // Field name: point
  {
    size_t item_size = sizeof(ros_message->point);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  // Field name: nu
  {
    size_t item_size = sizeof(ros_message->nu);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  // Field name: eta
  {
    size_t item_size = sizeof(ros_message->eta);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_ngc_interfaces
size_t max_serialized_size_key_ngc_interfaces__msg__HMI(
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
  // Field name: mode
  {
    size_t array_size = 1;
    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Field name: route
  {
    size_t array_size = 1;
    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }

  // Field name: point
  {
    size_t array_size = 1;
    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }

  // Field name: nu
  {
    size_t array_size = 1;
    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Field name: eta
  {
    size_t array_size = 1;
    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  size_t ret_val = current_alignment - initial_alignment;
  if (is_plain) {
    // All members are plain, and type is not empty.
    // We still need to check that the in-memory alignment
    // is the same as the CDR mandated alignment.
    using DataType = ngc_interfaces__msg__HMI;
    is_plain =
      (
      offsetof(DataType, eta) +
      last_member_size
      ) == ret_val;
  }
  return ret_val;
}


static bool _HMI__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const ngc_interfaces__msg__HMI * ros_message = static_cast<const ngc_interfaces__msg__HMI *>(untyped_ros_message);
  (void)ros_message;
  return cdr_serialize_ngc_interfaces__msg__HMI(ros_message, cdr);
}

static bool _HMI__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  ngc_interfaces__msg__HMI * ros_message = static_cast<ngc_interfaces__msg__HMI *>(untyped_ros_message);
  (void)ros_message;
  return cdr_deserialize_ngc_interfaces__msg__HMI(cdr, ros_message);
}

static uint32_t _HMI__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_ngc_interfaces__msg__HMI(
      untyped_ros_message, 0));
}

static size_t _HMI__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_ngc_interfaces__msg__HMI(
    full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}


static message_type_support_callbacks_t __callbacks_HMI = {
  "ngc_interfaces::msg",
  "HMI",
  _HMI__cdr_serialize,
  _HMI__cdr_deserialize,
  _HMI__get_serialized_size,
  _HMI__max_serialized_size,
  nullptr
};

static rosidl_message_type_support_t _HMI__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_HMI,
  get_message_typesupport_handle_function,
  &ngc_interfaces__msg__HMI__get_type_hash,
  &ngc_interfaces__msg__HMI__get_type_description,
  &ngc_interfaces__msg__HMI__get_type_description_sources,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, ngc_interfaces, msg, HMI)() {
  return &_HMI__type_support;
}

#if defined(__cplusplus)
}
#endif
