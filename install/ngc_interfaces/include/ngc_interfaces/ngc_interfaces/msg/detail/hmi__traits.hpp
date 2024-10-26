// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from ngc_interfaces:msg/HMI.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "ngc_interfaces/msg/hmi.hpp"


#ifndef NGC_INTERFACES__MSG__DETAIL__HMI__TRAITS_HPP_
#define NGC_INTERFACES__MSG__DETAIL__HMI__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "ngc_interfaces/msg/detail/hmi__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace ngc_interfaces
{

namespace msg
{

inline void to_flow_style_yaml(
  const HMI & msg,
  std::ostream & out)
{
  out << "{";
  // member: mode
  {
    out << "mode: ";
    rosidl_generator_traits::value_to_yaml(msg.mode, out);
    out << ", ";
  }

  // member: route
  {
    out << "route: ";
    rosidl_generator_traits::value_to_yaml(msg.route, out);
    out << ", ";
  }

  // member: point
  {
    out << "point: ";
    rosidl_generator_traits::value_to_yaml(msg.point, out);
    out << ", ";
  }

  // member: nu
  {
    out << "nu: ";
    rosidl_generator_traits::value_to_yaml(msg.nu, out);
    out << ", ";
  }

  // member: eta
  {
    out << "eta: ";
    rosidl_generator_traits::value_to_yaml(msg.eta, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const HMI & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: mode
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "mode: ";
    rosidl_generator_traits::value_to_yaml(msg.mode, out);
    out << "\n";
  }

  // member: route
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "route: ";
    rosidl_generator_traits::value_to_yaml(msg.route, out);
    out << "\n";
  }

  // member: point
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "point: ";
    rosidl_generator_traits::value_to_yaml(msg.point, out);
    out << "\n";
  }

  // member: nu
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "nu: ";
    rosidl_generator_traits::value_to_yaml(msg.nu, out);
    out << "\n";
  }

  // member: eta
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "eta: ";
    rosidl_generator_traits::value_to_yaml(msg.eta, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const HMI & msg, bool use_flow_style = false)
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
  const ngc_interfaces::msg::HMI & msg,
  std::ostream & out, size_t indentation = 0)
{
  ngc_interfaces::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use ngc_interfaces::msg::to_yaml() instead")]]
inline std::string to_yaml(const ngc_interfaces::msg::HMI & msg)
{
  return ngc_interfaces::msg::to_yaml(msg);
}

template<>
inline const char * data_type<ngc_interfaces::msg::HMI>()
{
  return "ngc_interfaces::msg::HMI";
}

template<>
inline const char * name<ngc_interfaces::msg::HMI>()
{
  return "ngc_interfaces/msg/HMI";
}

template<>
struct has_fixed_size<ngc_interfaces::msg::HMI>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<ngc_interfaces::msg::HMI>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<ngc_interfaces::msg::HMI>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // NGC_INTERFACES__MSG__DETAIL__HMI__TRAITS_HPP_
