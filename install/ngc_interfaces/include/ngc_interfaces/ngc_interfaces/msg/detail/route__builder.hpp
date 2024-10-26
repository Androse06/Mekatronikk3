// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from ngc_interfaces:msg/Route.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "ngc_interfaces/msg/route.hpp"


#ifndef NGC_INTERFACES__MSG__DETAIL__ROUTE__BUILDER_HPP_
#define NGC_INTERFACES__MSG__DETAIL__ROUTE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "ngc_interfaces/msg/detail/route__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace ngc_interfaces
{

namespace msg
{

namespace builder
{

class Init_Route_waypoints
{
public:
  explicit Init_Route_waypoints(::ngc_interfaces::msg::Route & msg)
  : msg_(msg)
  {}
  ::ngc_interfaces::msg::Route waypoints(::ngc_interfaces::msg::Route::_waypoints_type arg)
  {
    msg_.waypoints = std::move(arg);
    return std::move(msg_);
  }

private:
  ::ngc_interfaces::msg::Route msg_;
};

class Init_Route_route_name
{
public:
  Init_Route_route_name()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Route_waypoints route_name(::ngc_interfaces::msg::Route::_route_name_type arg)
  {
    msg_.route_name = std::move(arg);
    return Init_Route_waypoints(msg_);
  }

private:
  ::ngc_interfaces::msg::Route msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::ngc_interfaces::msg::Route>()
{
  return ngc_interfaces::msg::builder::Init_Route_route_name();
}

}  // namespace ngc_interfaces

#endif  // NGC_INTERFACES__MSG__DETAIL__ROUTE__BUILDER_HPP_
