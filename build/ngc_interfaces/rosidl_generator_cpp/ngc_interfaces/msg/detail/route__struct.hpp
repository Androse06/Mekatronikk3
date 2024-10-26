// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from ngc_interfaces:msg/Route.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "ngc_interfaces/msg/route.hpp"


#ifndef NGC_INTERFACES__MSG__DETAIL__ROUTE__STRUCT_HPP_
#define NGC_INTERFACES__MSG__DETAIL__ROUTE__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'waypoints'
#include "ngc_interfaces/msg/detail/waypoint__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__ngc_interfaces__msg__Route __attribute__((deprecated))
#else
# define DEPRECATED__ngc_interfaces__msg__Route __declspec(deprecated)
#endif

namespace ngc_interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct Route_
{
  using Type = Route_<ContainerAllocator>;

  explicit Route_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->route_name = "";
    }
  }

  explicit Route_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : route_name(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->route_name = "";
    }
  }

  // field types and members
  using _route_name_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _route_name_type route_name;
  using _waypoints_type =
    std::vector<ngc_interfaces::msg::Waypoint_<ContainerAllocator>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<ngc_interfaces::msg::Waypoint_<ContainerAllocator>>>;
  _waypoints_type waypoints;

  // setters for named parameter idiom
  Type & set__route_name(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->route_name = _arg;
    return *this;
  }
  Type & set__waypoints(
    const std::vector<ngc_interfaces::msg::Waypoint_<ContainerAllocator>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<ngc_interfaces::msg::Waypoint_<ContainerAllocator>>> & _arg)
  {
    this->waypoints = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    ngc_interfaces::msg::Route_<ContainerAllocator> *;
  using ConstRawPtr =
    const ngc_interfaces::msg::Route_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<ngc_interfaces::msg::Route_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<ngc_interfaces::msg::Route_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      ngc_interfaces::msg::Route_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<ngc_interfaces::msg::Route_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      ngc_interfaces::msg::Route_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<ngc_interfaces::msg::Route_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<ngc_interfaces::msg::Route_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<ngc_interfaces::msg::Route_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__ngc_interfaces__msg__Route
    std::shared_ptr<ngc_interfaces::msg::Route_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__ngc_interfaces__msg__Route
    std::shared_ptr<ngc_interfaces::msg::Route_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Route_ & other) const
  {
    if (this->route_name != other.route_name) {
      return false;
    }
    if (this->waypoints != other.waypoints) {
      return false;
    }
    return true;
  }
  bool operator!=(const Route_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Route_

// alias to use template instance with default allocator
using Route =
  ngc_interfaces::msg::Route_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace ngc_interfaces

#endif  // NGC_INTERFACES__MSG__DETAIL__ROUTE__STRUCT_HPP_
