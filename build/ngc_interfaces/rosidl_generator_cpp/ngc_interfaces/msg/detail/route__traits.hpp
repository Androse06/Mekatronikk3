// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from ngc_interfaces:msg/Route.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "ngc_interfaces/msg/route.hpp"


#ifndef NGC_INTERFACES__MSG__DETAIL__ROUTE__TRAITS_HPP_
#define NGC_INTERFACES__MSG__DETAIL__ROUTE__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "ngc_interfaces/msg/detail/route__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'waypoints'
#include "ngc_interfaces/msg/detail/waypoint__traits.hpp"

namespace ngc_interfaces
{

namespace msg
{

inline void to_flow_style_yaml(
  const Route & msg,
  std::ostream & out)
{
  out << "{";
  // member: route_name
  {
    out << "route_name: ";
    rosidl_generator_traits::value_to_yaml(msg.route_name, out);
    out << ", ";
  }

  // member: waypoints
  {
    if (msg.waypoints.size() == 0) {
      out << "waypoints: []";
    } else {
      out << "waypoints: [";
      size_t pending_items = msg.waypoints.size();
      for (auto item : msg.waypoints) {
        to_flow_style_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Route & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: route_name
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "route_name: ";
    rosidl_generator_traits::value_to_yaml(msg.route_name, out);
    out << "\n";
  }

  // member: waypoints
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.waypoints.size() == 0) {
      out << "waypoints: []\n";
    } else {
      out << "waypoints:\n";
      for (auto item : msg.waypoints) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "-\n";
        to_block_style_yaml(item, out, indentation + 2);
      }
    }
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Route & msg, bool use_flow_style = false)
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
  const ngc_interfaces::msg::Route & msg,
  std::ostream & out, size_t indentation = 0)
{
  ngc_interfaces::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use ngc_interfaces::msg::to_yaml() instead")]]
inline std::string to_yaml(const ngc_interfaces::msg::Route & msg)
{
  return ngc_interfaces::msg::to_yaml(msg);
}

template<>
inline const char * data_type<ngc_interfaces::msg::Route>()
{
  return "ngc_interfaces::msg::Route";
}

template<>
inline const char * name<ngc_interfaces::msg::Route>()
{
  return "ngc_interfaces/msg/Route";
}

template<>
struct has_fixed_size<ngc_interfaces::msg::Route>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<ngc_interfaces::msg::Route>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<ngc_interfaces::msg::Route>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // NGC_INTERFACES__MSG__DETAIL__ROUTE__TRAITS_HPP_
