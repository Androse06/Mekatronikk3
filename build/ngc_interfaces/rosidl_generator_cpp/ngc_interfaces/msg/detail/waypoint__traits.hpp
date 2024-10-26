// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from ngc_interfaces:msg/Waypoint.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "ngc_interfaces/msg/waypoint.hpp"


#ifndef NGC_INTERFACES__MSG__DETAIL__WAYPOINT__TRAITS_HPP_
#define NGC_INTERFACES__MSG__DETAIL__WAYPOINT__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "ngc_interfaces/msg/detail/waypoint__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace ngc_interfaces
{

namespace msg
{

inline void to_flow_style_yaml(
  const Waypoint & msg,
  std::ostream & out)
{
  out << "{";
  // member: latitude
  {
    out << "latitude: ";
    rosidl_generator_traits::value_to_yaml(msg.latitude, out);
    out << ", ";
  }

  // member: longitude
  {
    out << "longitude: ";
    rosidl_generator_traits::value_to_yaml(msg.longitude, out);
    out << ", ";
  }

  // member: name
  {
    out << "name: ";
    rosidl_generator_traits::value_to_yaml(msg.name, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Waypoint & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: latitude
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "latitude: ";
    rosidl_generator_traits::value_to_yaml(msg.latitude, out);
    out << "\n";
  }

  // member: longitude
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "longitude: ";
    rosidl_generator_traits::value_to_yaml(msg.longitude, out);
    out << "\n";
  }

  // member: name
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "name: ";
    rosidl_generator_traits::value_to_yaml(msg.name, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Waypoint & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace ngc_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use ngc_interfaces::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const ngc_interfaces::msg::Waypoint & msg,
  std::ostream & out, size_t indentation = 0)
{
  ngc_interfaces::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use ngc_interfaces::msg::to_yaml() instead")]]
inline std::string to_yaml(const ngc_interfaces::msg::Waypoint & msg)
{
  return ngc_interfaces::msg::to_yaml(msg);
}

template<>
inline const char * data_type<ngc_interfaces::msg::Waypoint>()
{
  return "ngc_interfaces::msg::Waypoint";
}

template<>
inline const char * name<ngc_interfaces::msg::Waypoint>()
{
  return "ngc_interfaces/msg/Waypoint";
}

template<>
struct has_fixed_size<ngc_interfaces::msg::Waypoint>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<ngc_interfaces::msg::Waypoint>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<ngc_interfaces::msg::Waypoint>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // NGC_INTERFACES__MSG__DETAIL__WAYPOINT__TRAITS_HPP_
