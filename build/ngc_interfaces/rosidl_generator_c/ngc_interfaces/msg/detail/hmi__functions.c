// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from ngc_interfaces:msg/HMI.idl
// generated code does not contain a copyright notice
#include "ngc_interfaces/msg/detail/hmi__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
ngc_interfaces__msg__HMI__init(ngc_interfaces__msg__HMI * msg)
{
  if (!msg) {
    return false;
  }
  // mode
  // route
  // point
  // nu
  // eta
  return true;
}

void
ngc_interfaces__msg__HMI__fini(ngc_interfaces__msg__HMI * msg)
{
  if (!msg) {
    return;
  }
  // mode
  // route
  // point
  // nu
  // eta
}

bool
ngc_interfaces__msg__HMI__are_equal(const ngc_interfaces__msg__HMI * lhs, const ngc_interfaces__msg__HMI * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // mode
  if (lhs->mode != rhs->mode) {
    return false;
  }
  // route
  if (lhs->route != rhs->route) {
    return false;
  }
  // point
  if (lhs->point != rhs->point) {
    return false;
  }
  // nu
  if (lhs->nu != rhs->nu) {
    return false;
  }
  // eta
  if (lhs->eta != rhs->eta) {
    return false;
  }
  return true;
}

bool
ngc_interfaces__msg__HMI__copy(
  const ngc_interfaces__msg__HMI * input,
  ngc_interfaces__msg__HMI * output)
{
  if (!input || !output) {
    return false;
  }
  // mode
  output->mode = input->mode;
  // route
  output->route = input->route;
  // point
  output->point = input->point;
  // nu
  output->nu = input->nu;
  // eta
  output->eta = input->eta;
  return true;
}

ngc_interfaces__msg__HMI *
ngc_interfaces__msg__HMI__create(void)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  ngc_interfaces__msg__HMI * msg = (ngc_interfaces__msg__HMI *)allocator.allocate(sizeof(ngc_interfaces__msg__HMI), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(ngc_interfaces__msg__HMI));
  bool success = ngc_interfaces__msg__HMI__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
ngc_interfaces__msg__HMI__destroy(ngc_interfaces__msg__HMI * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    ngc_interfaces__msg__HMI__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
ngc_interfaces__msg__HMI__Sequence__init(ngc_interfaces__msg__HMI__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  ngc_interfaces__msg__HMI * data = NULL;

  if (size) {
    data = (ngc_interfaces__msg__HMI *)allocator.zero_allocate(size, sizeof(ngc_interfaces__msg__HMI), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = ngc_interfaces__msg__HMI__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        ngc_interfaces__msg__HMI__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
ngc_interfaces__msg__HMI__Sequence__fini(ngc_interfaces__msg__HMI__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      ngc_interfaces__msg__HMI__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

ngc_interfaces__msg__HMI__Sequence *
ngc_interfaces__msg__HMI__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  ngc_interfaces__msg__HMI__Sequence * array = (ngc_interfaces__msg__HMI__Sequence *)allocator.allocate(sizeof(ngc_interfaces__msg__HMI__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = ngc_interfaces__msg__HMI__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
ngc_interfaces__msg__HMI__Sequence__destroy(ngc_interfaces__msg__HMI__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    ngc_interfaces__msg__HMI__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
ngc_interfaces__msg__HMI__Sequence__are_equal(const ngc_interfaces__msg__HMI__Sequence * lhs, const ngc_interfaces__msg__HMI__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!ngc_interfaces__msg__HMI__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
ngc_interfaces__msg__HMI__Sequence__copy(
  const ngc_interfaces__msg__HMI__Sequence * input,
  ngc_interfaces__msg__HMI__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(ngc_interfaces__msg__HMI);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    ngc_interfaces__msg__HMI * data =
      (ngc_interfaces__msg__HMI *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!ngc_interfaces__msg__HMI__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          ngc_interfaces__msg__HMI__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!ngc_interfaces__msg__HMI__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
