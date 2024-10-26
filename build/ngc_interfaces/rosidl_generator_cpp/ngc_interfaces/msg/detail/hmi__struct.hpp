// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from ngc_interfaces:msg/HMI.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "ngc_interfaces/msg/hmi.hpp"


#ifndef NGC_INTERFACES__MSG__DETAIL__HMI__STRUCT_HPP_
#define NGC_INTERFACES__MSG__DETAIL__HMI__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__ngc_interfaces__msg__HMI __attribute__((deprecated))
#else
# define DEPRECATED__ngc_interfaces__msg__HMI __declspec(deprecated)
#endif

namespace ngc_interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct HMI_
{
  using Type = HMI_<ContainerAllocator>;

  explicit HMI_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->mode = 0l;
      this->route = false;
      this->point = false;
      this->nu = 0.0f;
      this->eta = 0.0f;
    }
  }

  explicit HMI_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->mode = 0l;
      this->route = false;
      this->point = false;
      this->nu = 0.0f;
      this->eta = 0.0f;
    }
  }

  // field types and members
  using _mode_type =
    int32_t;
  _mode_type mode;
  using _route_type =
    bool;
  _route_type route;
  using _point_type =
    bool;
  _point_type point;
  using _nu_type =
    float;
  _nu_type nu;
  using _eta_type =
    float;
  _eta_type eta;

  // setters for named parameter idiom
  Type & set__mode(
    const int32_t & _arg)
  {
    this->mode = _arg;
    return *this;
  }
  Type & set__route(
    const bool & _arg)
  {
    this->route = _arg;
    return *this;
  }
  Type & set__point(
    const bool & _arg)
  {
    this->point = _arg;
    return *this;
  }
  Type & set__nu(
    const float & _arg)
  {
    this->nu = _arg;
    return *this;
  }
  Type & set__eta(
    const float & _arg)
  {
    this->eta = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    ngc_interfaces::msg::HMI_<ContainerAllocator> *;
  using ConstRawPtr =
    const ngc_interfaces::msg::HMI_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<ngc_interfaces::msg::HMI_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<ngc_interfaces::msg::HMI_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      ngc_interfaces::msg::HMI_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<ngc_interfaces::msg::HMI_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      ngc_interfaces::msg::HMI_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<ngc_interfaces::msg::HMI_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<ngc_interfaces::msg::HMI_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<ngc_interfaces::msg::HMI_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__ngc_interfaces__msg__HMI
    std::shared_ptr<ngc_interfaces::msg::HMI_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__ngc_interfaces__msg__HMI
    std::shared_ptr<ngc_interfaces::msg::HMI_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const HMI_ & other) const
  {
    if (this->mode != other.mode) {
      return false;
    }
    if (this->route != other.route) {
      return false;
    }
    if (this->point != other.point) {
      return false;
    }
    if (this->nu != other.nu) {
      return false;
    }
    if (this->eta != other.eta) {
      return false;
    }
    return true;
  }
  bool operator!=(const HMI_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct HMI_

// alias to use template instance with default allocator
using HMI =
  ngc_interfaces::msg::HMI_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace ngc_interfaces

#endif  // NGC_INTERFACES__MSG__DETAIL__HMI__STRUCT_HPP_
