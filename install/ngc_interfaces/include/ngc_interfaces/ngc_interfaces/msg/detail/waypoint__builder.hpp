// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from ngc_interfaces:msg/Waypoint.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "ngc_interfaces/msg/waypoint.hpp"


#ifndef NGC_INTERFACES__MSG__DETAIL__WAYPOINT__BUILDER_HPP_
#define NGC_INTERFACES__MSG__DETAIL__WAYPOINT__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "ngc_interfaces/msg/detail/waypoint__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace ngc_interfaces
{

namespace msg
{

namespace builder
{

class Init_Waypoint_name
{
public:
  explicit Init_Waypoint_name(::ngc_interfaces::msg::Waypoint & msg)
  : msg_(msg)
  {}
  ::ngc_interfaces::msg::Waypoint name(::ngc_interfaces::msg::Waypoint::_name_type arg)
  {
    msg_.name = std::move(arg);
    return std::move(msg_);
  }

private:
  ::ngc_interfaces::msg::Waypoint msg_;
};

class Init_Waypoint_longitude
{
public:
  explicit Init_Waypoint_longitude(::ngc_interfaces::msg::Waypoint & msg)
  : msg_(msg)
  {}
  Init_Waypoint_name longitude(::ngc_interfaces::msg::Waypoint::_longitude_type arg)
  {
    msg_.longitude = std::move(arg);
    return Init_Waypoint_name(msg_);
  }

private:
  ::ngc_interfaces::msg::Waypoint msg_;
};

class Init_Waypoint_latitude
{
public:
  Init_Waypoint_latitude()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Waypoint_longitude latitude(::ngc_interfaces::msg::Waypoint::_latitude_type arg)
  {
    msg_.latitude = std::move(arg);
    return Init_Waypoint_longitude(msg_);
  }

private:
  ::ngc_interfaces::msg::Waypoint msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::ngc_interfaces::msg::Waypoint>()
{
  return ngc_interfaces::msg::builder::Init_Waypoint_latitude();
}

}  // namespace ngc_interfaces

#endif  // NGC_INTERFACES__MSG__DETAIL__WAYPOINT__BUILDER_HPP_
