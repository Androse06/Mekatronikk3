// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__type_support.cpp.em
// with input from ngc_interfaces:msg/Tau.idl
// generated code does not contain a copyright notice
#include "ngc_interfaces/msg/detail/tau__rosidl_typesupport_fastrtps_cpp.hpp"
#include "ngc_interfaces/msg/detail/tau__functions.h"
#include "ngc_interfaces/msg/detail/tau__struct.hpp"

#include <cstddef>
#include <limits>
#include <stdexcept>
#include <string>
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_fastrtps_cpp/identifier.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_fastrtps_cpp/serialization_helpers.hpp"
#include "rosidl_typesupport_fastrtps_cpp/wstring_conversion.hpp"
#include "fastcdr/Cdr.h"


// forward declaration of message dependencies and their conversion functions

namespace ngc_interfaces
{

namespace msg
{

namespace typesupport_fastrtps_cpp
{


bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_ngc_interfaces
cdr_serialize(
  const ngc_interfaces::msg::Tau & ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  // Member: surge_x
  cdr << ros_message.surge_x;

  // Member: surge_y
  cdr << ros_message.surge_y;

  // Member: sway_y
  cdr << ros_message.sway_y;

  // Member: heave_z
  cdr << ros_message.heave_z;

  // Member: roll_k
  cdr << ros_message.roll_k;

  // Member: pitch_m
  cdr << ros_message.pitch_m;

  // Member: yaw_n
  cdr << ros_message.yaw_n;

  return true;
}

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_ngc_interfaces
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  ngc_interfaces::msg::Tau & ros_message)
{
  // Member: surge_x
  cdr >> ros_message.surge_x;

  // Member: surge_y
  cdr >> ros_message.surge_y;

  // Member: sway_y
  cdr >> ros_message.sway_y;

  // Member: heave_z
  cdr >> ros_message.heave_z;

  // Member: roll_k
  cdr >> ros_message.roll_k;

  // Member: pitch_m
  cdr >> ros_message.pitch_m;

  // Member: yaw_n
  cdr >> ros_message.yaw_n;

  return true;
}


size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_ngc_interfaces
get_serialized_size(
  const ngc_interfaces::msg::Tau & ros_message,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // Member: surge_x
  {
    size_t item_size = sizeof(ros_message.surge_x);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  // Member: surge_y
  {
    size_t item_size = sizeof(ros_message.surge_y);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  // Member: sway_y
  {
    size_t item_size = sizeof(ros_message.sway_y);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  // Member: heave_z
  {
    size_t item_size = sizeof(ros_message.heave_z);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  // Member: roll_k
  {
    size_t item_size = sizeof(ros_message.roll_k);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  // Member: pitch_m
  {
    size_t item_size = sizeof(ros_message.pitch_m);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  // Member: yaw_n
  {
    size_t item_size = sizeof(ros_message.yaw_n);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}


size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_ngc_interfaces
max_serialized_size_Tau(
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

  // Member: surge_x
  {
    size_t array_size = 1;
    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // Member: surge_y
  {
    size_t array_size = 1;
    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // Member: sway_y
  {
    size_t array_size = 1;
    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // Member: heave_z
  {
    size_t array_size = 1;
    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // Member: roll_k
  {
    size_t array_size = 1;
    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // Member: pitch_m
  {
    size_t array_size = 1;
    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // Member: yaw_n
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
    using DataType = ngc_interfaces::msg::Tau;
    is_plain =
      (
      offsetof(DataType, yaw_n) +
      last_member_size
      ) == ret_val;
  }

  return ret_val;
}

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_ngc_interfaces
cdr_serialize_key(
  const ngc_interfaces::msg::Tau & ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  // Member: surge_x
  cdr << ros_message.surge_x;

  // Member: surge_y
  cdr << ros_message.surge_y;

  // Member: sway_y
  cdr << ros_message.sway_y;

  // Member: heave_z
  cdr << ros_message.heave_z;

  // Member: roll_k
  cdr << ros_message.roll_k;

  // Member: pitch_m
  cdr << ros_message.pitch_m;

  // Member: yaw_n
  cdr << ros_message.yaw_n;

  return true;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_ngc_interfaces
get_serialized_size_key(
  const ngc_interfaces::msg::Tau & ros_message,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // Member: surge_x
  {
    size_t item_size = sizeof(ros_message.surge_x);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  // Member: surge_y
  {
    size_t item_size = sizeof(ros_message.surge_y);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  // Member: sway_y
  {
    size_t item_size = sizeof(ros_message.sway_y);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  // Member: heave_z
  {
    size_t item_size = sizeof(ros_message.heave_z);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  // Member: roll_k
  {
    size_t item_size = sizeof(ros_message.roll_k);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  // Member: pitch_m
  {
    size_t item_size = sizeof(ros_message.pitch_m);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  // Member: yaw_n
  {
    size_t item_size = sizeof(ros_message.yaw_n);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_ngc_interfaces
max_serialized_size_key_Tau(
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

  // Member: surge_x
  {
    size_t array_size = 1;
    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: surge_y
  {
    size_t array_size = 1;
    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: sway_y
  {
    size_t array_size = 1;
    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: heave_z
  {
    size_t array_size = 1;
    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: roll_k
  {
    size_t array_size = 1;
    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: pitch_m
  {
    size_t array_size = 1;
    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: yaw_n
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
    using DataType = ngc_interfaces::msg::Tau;
    is_plain =
      (
      offsetof(DataType, yaw_n) +
      last_member_size
      ) == ret_val;
  }

  return ret_val;
}


static bool _Tau__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  auto typed_message =
    static_cast<const ngc_interfaces::msg::Tau *>(
    untyped_ros_message);
  return cdr_serialize(*typed_message, cdr);
}

static bool _Tau__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  auto typed_message =
    static_cast<ngc_interfaces::msg::Tau *>(
    untyped_ros_message);
  return cdr_deserialize(cdr, *typed_message);
}

static uint32_t _Tau__get_serialized_size(
  const void * untyped_ros_message)
{
  auto typed_message =
    static_cast<const ngc_interfaces::msg::Tau *>(
    untyped_ros_message);
  return static_cast<uint32_t>(get_serialized_size(*typed_message, 0));
}

static size_t _Tau__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_Tau(full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}

static message_type_support_callbacks_t _Tau__callbacks = {
  "ngc_interfaces::msg",
  "Tau",
  _Tau__cdr_serialize,
  _Tau__cdr_deserialize,
  _Tau__get_serialized_size,
  _Tau__max_serialized_size,
  nullptr
};

static rosidl_message_type_support_t _Tau__handle = {
  rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
  &_Tau__callbacks,
  get_message_typesupport_handle_function,
  &ngc_interfaces__msg__Tau__get_type_hash,
  &ngc_interfaces__msg__Tau__get_type_description,
  &ngc_interfaces__msg__Tau__get_type_description_sources,
};

}  // namespace typesupport_fastrtps_cpp

}  // namespace msg

}  // namespace ngc_interfaces

namespace rosidl_typesupport_fastrtps_cpp
{

template<>
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_EXPORT_ngc_interfaces
const rosidl_message_type_support_t *
get_message_type_support_handle<ngc_interfaces::msg::Tau>()
{
  return &ngc_interfaces::msg::typesupport_fastrtps_cpp::_Tau__handle;
}

}  // namespace rosidl_typesupport_fastrtps_cpp

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, ngc_interfaces, msg, Tau)() {
  return &ngc_interfaces::msg::typesupport_fastrtps_cpp::_Tau__handle;
}

#ifdef __cplusplus
}
#endif
