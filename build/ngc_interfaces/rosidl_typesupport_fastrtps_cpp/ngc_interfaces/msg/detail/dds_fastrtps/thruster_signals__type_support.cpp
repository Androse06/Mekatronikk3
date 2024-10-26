// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__type_support.cpp.em
// with input from ngc_interfaces:msg/ThrusterSignals.idl
// generated code does not contain a copyright notice
#include "ngc_interfaces/msg/detail/thruster_signals__rosidl_typesupport_fastrtps_cpp.hpp"
#include "ngc_interfaces/msg/detail/thruster_signals__functions.h"
#include "ngc_interfaces/msg/detail/thruster_signals__struct.hpp"

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
  const ngc_interfaces::msg::ThrusterSignals & ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  // Member: thruster_id
  cdr << ros_message.thruster_id;

  // Member: rps
  cdr << ros_message.rps;

  // Member: pitch
  cdr << ros_message.pitch;

  // Member: azimuth_deg
  cdr << ros_message.azimuth_deg;

  // Member: active
  cdr << (ros_message.active ? true : false);

  // Member: error
  cdr << (ros_message.error ? true : false);

  return true;
}

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_ngc_interfaces
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  ngc_interfaces::msg::ThrusterSignals & ros_message)
{
  // Member: thruster_id
  cdr >> ros_message.thruster_id;

  // Member: rps
  cdr >> ros_message.rps;

  // Member: pitch
  cdr >> ros_message.pitch;

  // Member: azimuth_deg
  cdr >> ros_message.azimuth_deg;

  // Member: active
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message.active = tmp ? true : false;
  }

  // Member: error
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message.error = tmp ? true : false;
  }

  return true;
}


size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_ngc_interfaces
get_serialized_size(
  const ngc_interfaces::msg::ThrusterSignals & ros_message,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // Member: thruster_id
  {
    size_t item_size = sizeof(ros_message.thruster_id);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  // Member: rps
  {
    size_t item_size = sizeof(ros_message.rps);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  // Member: pitch
  {
    size_t item_size = sizeof(ros_message.pitch);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  // Member: azimuth_deg
  {
    size_t item_size = sizeof(ros_message.azimuth_deg);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  // Member: active
  {
    size_t item_size = sizeof(ros_message.active);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  // Member: error
  {
    size_t item_size = sizeof(ros_message.error);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}


size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_ngc_interfaces
max_serialized_size_ThrusterSignals(
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

  // Member: thruster_id
  {
    size_t array_size = 1;
    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // Member: rps
  {
    size_t array_size = 1;
    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // Member: pitch
  {
    size_t array_size = 1;
    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // Member: azimuth_deg
  {
    size_t array_size = 1;
    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // Member: active
  {
    size_t array_size = 1;
    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }
  // Member: error
  {
    size_t array_size = 1;
    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }

  size_t ret_val = current_alignment - initial_alignment;
  if (is_plain) {
    // All members are plain, and type is not empty.
    // We still need to check that the in-memory alignment
    // is the same as the CDR mandated alignment.
    using DataType = ngc_interfaces::msg::ThrusterSignals;
    is_plain =
      (
      offsetof(DataType, error) +
      last_member_size
      ) == ret_val;
  }

  return ret_val;
}

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_ngc_interfaces
cdr_serialize_key(
  const ngc_interfaces::msg::ThrusterSignals & ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  // Member: thruster_id
  cdr << ros_message.thruster_id;

  // Member: rps
  cdr << ros_message.rps;

  // Member: pitch
  cdr << ros_message.pitch;

  // Member: azimuth_deg
  cdr << ros_message.azimuth_deg;

  // Member: active
  cdr << (ros_message.active ? true : false);

  // Member: error
  cdr << (ros_message.error ? true : false);

  return true;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_ngc_interfaces
get_serialized_size_key(
  const ngc_interfaces::msg::ThrusterSignals & ros_message,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // Member: thruster_id
  {
    size_t item_size = sizeof(ros_message.thruster_id);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  // Member: rps
  {
    size_t item_size = sizeof(ros_message.rps);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  // Member: pitch
  {
    size_t item_size = sizeof(ros_message.pitch);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  // Member: azimuth_deg
  {
    size_t item_size = sizeof(ros_message.azimuth_deg);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  // Member: active
  {
    size_t item_size = sizeof(ros_message.active);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  // Member: error
  {
    size_t item_size = sizeof(ros_message.error);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_ngc_interfaces
max_serialized_size_key_ThrusterSignals(
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

  // Member: thruster_id
  {
    size_t array_size = 1;
    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: rps
  {
    size_t array_size = 1;
    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Member: pitch
  {
    size_t array_size = 1;
    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Member: azimuth_deg
  {
    size_t array_size = 1;
    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Member: active
  {
    size_t array_size = 1;
    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }

  // Member: error
  {
    size_t array_size = 1;
    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }

  size_t ret_val = current_alignment - initial_alignment;
  if (is_plain) {
    // All members are plain, and type is not empty.
    // We still need to check that the in-memory alignment
    // is the same as the CDR mandated alignment.
    using DataType = ngc_interfaces::msg::ThrusterSignals;
    is_plain =
      (
      offsetof(DataType, error) +
      last_member_size
      ) == ret_val;
  }

  return ret_val;
}


static bool _ThrusterSignals__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  auto typed_message =
    static_cast<const ngc_interfaces::msg::ThrusterSignals *>(
    untyped_ros_message);
  return cdr_serialize(*typed_message, cdr);
}

static bool _ThrusterSignals__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  auto typed_message =
    static_cast<ngc_interfaces::msg::ThrusterSignals *>(
    untyped_ros_message);
  return cdr_deserialize(cdr, *typed_message);
}

static uint32_t _ThrusterSignals__get_serialized_size(
  const void * untyped_ros_message)
{
  auto typed_message =
    static_cast<const ngc_interfaces::msg::ThrusterSignals *>(
    untyped_ros_message);
  return static_cast<uint32_t>(get_serialized_size(*typed_message, 0));
}

static size_t _ThrusterSignals__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_ThrusterSignals(full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}

static message_type_support_callbacks_t _ThrusterSignals__callbacks = {
  "ngc_interfaces::msg",
  "ThrusterSignals",
  _ThrusterSignals__cdr_serialize,
  _ThrusterSignals__cdr_deserialize,
  _ThrusterSignals__get_serialized_size,
  _ThrusterSignals__max_serialized_size,
  nullptr
};

static rosidl_message_type_support_t _ThrusterSignals__handle = {
  rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
  &_ThrusterSignals__callbacks,
  get_message_typesupport_handle_function,
  &ngc_interfaces__msg__ThrusterSignals__get_type_hash,
  &ngc_interfaces__msg__ThrusterSignals__get_type_description,
  &ngc_interfaces__msg__ThrusterSignals__get_type_description_sources,
};

}  // namespace typesupport_fastrtps_cpp

}  // namespace msg

}  // namespace ngc_interfaces

namespace rosidl_typesupport_fastrtps_cpp
{

template<>
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_EXPORT_ngc_interfaces
const rosidl_message_type_support_t *
get_message_type_support_handle<ngc_interfaces::msg::ThrusterSignals>()
{
  return &ngc_interfaces::msg::typesupport_fastrtps_cpp::_ThrusterSignals__handle;
}

}  // namespace rosidl_typesupport_fastrtps_cpp

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, ngc_interfaces, msg, ThrusterSignals)() {
  return &ngc_interfaces::msg::typesupport_fastrtps_cpp::_ThrusterSignals__handle;
}

#ifdef __cplusplus
}
#endif
