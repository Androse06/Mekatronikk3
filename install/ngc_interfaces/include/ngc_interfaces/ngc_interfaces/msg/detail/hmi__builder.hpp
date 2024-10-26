// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from ngc_interfaces:msg/HMI.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "ngc_interfaces/msg/hmi.hpp"


#ifndef NGC_INTERFACES__MSG__DETAIL__HMI__BUILDER_HPP_
#define NGC_INTERFACES__MSG__DETAIL__HMI__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "ngc_interfaces/msg/detail/hmi__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace ngc_interfaces
{

namespace msg
{

namespace builder
{

class Init_HMI_eta
{
public:
  explicit Init_HMI_eta(::ngc_interfaces::msg::HMI & msg)
  : msg_(msg)
  {}
  ::ngc_interfaces::msg::HMI eta(::ngc_interfaces::msg::HMI::_eta_type arg)
  {
    msg_.eta = std::move(arg);
    return std::move(msg_);
  }

private:
  ::ngc_interfaces::msg::HMI msg_;
};

class Init_HMI_nu
{
public:
  explicit Init_HMI_nu(::ngc_interfaces::msg::HMI & msg)
  : msg_(msg)
  {}
  Init_HMI_eta nu(::ngc_interfaces::msg::HMI::_nu_type arg)
  {
    msg_.nu = std::move(arg);
    return Init_HMI_eta(msg_);
  }

private:
  ::ngc_interfaces::msg::HMI msg_;
};

class Init_HMI_point
{
public:
  explicit Init_HMI_point(::ngc_interfaces::msg::HMI & msg)
  : msg_(msg)
  {}
  Init_HMI_nu point(::ngc_interfaces::msg::HMI::_point_type arg)
  {
    msg_.point = std::move(arg);
    return Init_HMI_nu(msg_);
  }

private:
  ::ngc_interfaces::msg::HMI msg_;
};

class Init_HMI_route
{
public:
  explicit Init_HMI_route(::ngc_interfaces::msg::HMI & msg)
  : msg_(msg)
  {}
  Init_HMI_point route(::ngc_interfaces::msg::HMI::_route_type arg)
  {
    msg_.route = std::move(arg);
    return Init_HMI_point(msg_);
  }

private:
  ::ngc_interfaces::msg::HMI msg_;
};

class Init_HMI_mode
{
public:
  Init_HMI_mode()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_HMI_route mode(::ngc_interfaces::msg::HMI::_mode_type arg)
  {
    msg_.mode = std::move(arg);
    return Init_HMI_route(msg_);
  }

private:
  ::ngc_interfaces::msg::HMI msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::ngc_interfaces::msg::HMI>()
{
  return ngc_interfaces::msg::builder::Init_HMI_mode();
}

}  // namespace ngc_interfaces

#endif  // NGC_INTERFACES__MSG__DETAIL__HMI__BUILDER_HPP_
