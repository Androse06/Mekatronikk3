// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__type_support.cpp.em
// with input from ngc_interfaces:msg/NuDot.idl
// generated code does not contain a copyright notice
#include "ngc_interfaces/msg/detail/nu_dot__rosidl_typesupport_fastrtps_cpp.hpp"
#include "ngc_interfaces/msg/detail/nu_dot__functions.h"
#include "ngc_interfaces/msg/detail/nu_dot__struct.hpp"

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
  const ngc_interfaces::msg::NuDot & ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  // Member: u_dot
  cdr << ros_message.u_dot;

  // Member: v_dot
  cdr << ros_message.v_dot;

  // Member: w_dot
  cdr << ros_message.w_dot;

  // Member: p_dot
  cdr << ros_message.p_dot;

  // Member: q_dot
  cdr << ros_message.q_dot;

  // Member: r_dot
  cdr << ros_message.r_dot;

  return true;
}

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_ngc_interfaces
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  ngc_interfaces::msg::NuDot & ros_message)
{
  // Member: u_dot
  cdr >> ros_message.u_dot;

  // Member: v_dot
  cdr >> ros_message.v_dot;

  // Member: w_dot
  cdr >> ros_message.w_dot;

  // Member: p_dot
  cdr >> ros_message.p_dot;

  // Member: q_dot
  cdr >> ros_message.q_dot;

  // Member: r_dot
  cdr >> ros_message.r_dot;

  return true;
}


size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_ngc_interfaces
get_serialized_size(
  const ngc_interfaces::msg::NuDot & ros_message,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // Member: u_dot
  {
    size_t item_size = sizeof(ros_message.u_dot);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  // Member: v_dot
  {
    size_t item_size = sizeof(ros_message.v_dot);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  // Member: w_dot
  {
    size_t item_size = sizeof(ros_message.w_dot);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  // Member: p_dot
  {
    size_t item_size = sizeof(ros_message.p_dot);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  // Member: q_dot
  {
    size_t item_size = sizeof(ros_message.q_dot);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  // Member: r_dot
  {
    size_t item_size = sizeof(ros_message.r_dot);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}


size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_ngc_interfaces
max_serialized_size_NuDot(
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

  // Member: u_dot
  {
    size_t array_size = 1;
    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // Member: v_dot
  {
    size_t array_size = 1;
    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // Member: w_dot
  {
    size_t array_size = 1;
    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // Member: p_dot
  {
    size_t array_size = 1;
    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // Member: q_dot
  {
    size_t array_size = 1;
    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // Member: r_dot
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
    using DataType = ngc_interfaces::msg::NuDot;
    is_plain =
      (
      offsetof(DataType, r_dot) +
      last_member_size
      ) == ret_val;
  }

  return ret_val;
}

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_ngc_interfaces
cdr_serialize_key(
  const ngc_interfaces::msg::NuDot & ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  // Member: u_dot
  cdr << ros_message.u_dot;

  // Member: v_dot
  cdr << ros_message.v_dot;

  // Member: w_dot
  cdr << ros_message.w_dot;

  // Member: p_dot
  cdr << ros_message.p_dot;

  // Member: q_dot
  cdr << ros_message.q_dot;

  // Member: r_dot
  cdr << ros_message.r_dot;

  return true;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_ngc_interfaces
get_serialized_size_key(
  const ngc_interfaces::msg::NuDot & ros_message,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // Member: u_dot
  {
    size_t item_size = sizeof(ros_message.u_dot);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  // Member: v_dot
  {
    size_t item_size = sizeof(ros_message.v_dot);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  // Member: w_dot
  {
    size_t item_size = sizeof(ros_message.w_dot);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  // Member: p_dot
  {
    size_t item_size = sizeof(ros_message.p_dot);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  // Member: q_dot
  {
    size_t item_size = sizeof(ros_message.q_dot);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  // Member: r_dot
  {
    size_t item_size = sizeof(ros_message.r_dot);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_ngc_interfaces
max_serialized_size_key_NuDot(
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

  // Member: u_dot
  {
    size_t array_size = 1;
    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: v_dot
  {
    size_t array_size = 1;
    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: w_dot
  {
    size_t array_size = 1;
    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: p_dot
  {
    size_t array_size = 1;
    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: q_dot
  {
    size_t array_size = 1;
    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: r_dot
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
    using DataType = ngc_interfaces::msg::NuDot;
    is_plain =
      (
      offsetof(DataType, r_dot) +
      last_member_size
      ) == ret_val;
  }

  return ret_val;
}


static bool _NuDot__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  auto typed_message =
    static_cast<const ngc_interfaces::msg::NuDot *>(
    untyped_ros_message);
  return cdr_serialize(*typed_message, cdr);
}

static bool _NuDot__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  auto typed_message =
    static_cast<ngc_interfaces::msg::NuDot *>(
    untyped_ros_message);
  return cdr_deserialize(cdr, *typed_message);
}

static uint32_t _NuDot__get_serialized_size(
  const void * untyped_ros_message)
{
  auto typed_message =
    static_cast<const ngc_interfaces::msg::NuDot *>(
    untyped_ros_message);
  return static_cast<uint32_t>(get_serialized_size(*typed_message, 0));
}

static size_t _NuDot__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_NuDot(full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}

static message_type_support_callbacks_t _NuDot__callbacks = {
  "ngc_interfaces::msg",
  "NuDot",
  _NuDot__cdr_serialize,
  _NuDot__cdr_deserialize,
  _NuDot__get_serialized_size,
  _NuDot__max_serialized_size,
  nullptr
};

static rosidl_message_type_support_t _NuDot__handle = {
  rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
  &_NuDot__callbacks,
  get_message_typesupport_handle_function,
  &ngc_interfaces__msg__NuDot__get_type_hash,
  &ngc_interfaces__msg__NuDot__get_type_description,
  &ngc_interfaces__msg__NuDot__get_type_description_sources,
};

}  // namespace typesupport_fastrtps_cpp

}  // namespace msg

}  // namespace ngc_interfaces

namespace rosidl_typesupport_fastrtps_cpp
{

template<>
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_EXPORT_ngc_interfaces
const rosidl_message_type_support_t *
get_message_type_support_handle<ngc_interfaces::msg::NuDot>()
{
  return &ngc_interfaces::msg::typesupport_fastrtps_cpp::_NuDot__handle;
}

}  // namespace rosidl_typesupport_fastrtps_cpp

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, ngc_interfaces, msg, NuDot)() {
  return &ngc_interfaces::msg::typesupport_fastrtps_cpp::_NuDot__handle;
}

#ifdef __cplusplus
}
#endif
