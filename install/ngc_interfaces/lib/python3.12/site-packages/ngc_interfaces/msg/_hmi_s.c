// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from ngc_interfaces:msg/HMI.idl
// generated code does not contain a copyright notice
#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <Python.h>
#include <stdbool.h>
#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-function"
#endif
#include "numpy/ndarrayobject.h"
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif
#include "rosidl_runtime_c/visibility_control.h"
#include "ngc_interfaces/msg/detail/hmi__struct.h"
#include "ngc_interfaces/msg/detail/hmi__functions.h"


ROSIDL_GENERATOR_C_EXPORT
bool ngc_interfaces__msg__hmi__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[28];
    {
      char * class_name = NULL;
      char * module_name = NULL;
      {
        PyObject * class_attr = PyObject_GetAttrString(_pymsg, "__class__");
        if (class_attr) {
          PyObject * name_attr = PyObject_GetAttrString(class_attr, "__name__");
          if (name_attr) {
            class_name = (char *)PyUnicode_1BYTE_DATA(name_attr);
            Py_DECREF(name_attr);
          }
          PyObject * module_attr = PyObject_GetAttrString(class_attr, "__module__");
          if (module_attr) {
            module_name = (char *)PyUnicode_1BYTE_DATA(module_attr);
            Py_DECREF(module_attr);
          }
          Py_DECREF(class_attr);
        }
      }
      if (!class_name || !module_name) {
        return false;
      }
      snprintf(full_classname_dest, sizeof(full_classname_dest), "%s.%s", module_name, class_name);
    }
    assert(strncmp("ngc_interfaces.msg._hmi.HMI", full_classname_dest, 27) == 0);
  }
  ngc_interfaces__msg__HMI * ros_message = _ros_message;
  {  // mode
    PyObject * field = PyObject_GetAttrString(_pymsg, "mode");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->mode = (int32_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }
  {  // route
    PyObject * field = PyObject_GetAttrString(_pymsg, "route");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->route = (Py_True == field);
    Py_DECREF(field);
  }
  {  // point
    PyObject * field = PyObject_GetAttrString(_pymsg, "point");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->point = (Py_True == field);
    Py_DECREF(field);
  }
  {  // nu
    PyObject * field = PyObject_GetAttrString(_pymsg, "nu");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->nu = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // eta
    PyObject * field = PyObject_GetAttrString(_pymsg, "eta");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->eta = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * ngc_interfaces__msg__hmi__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of HMI */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("ngc_interfaces.msg._hmi");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "HMI");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  ngc_interfaces__msg__HMI * ros_message = (ngc_interfaces__msg__HMI *)raw_ros_message;
  {  // mode
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->mode);
    {
      int rc = PyObject_SetAttrString(_pymessage, "mode", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // route
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->route ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "route", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // point
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->point ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "point", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // nu
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->nu);
    {
      int rc = PyObject_SetAttrString(_pymessage, "nu", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // eta
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->eta);
    {
      int rc = PyObject_SetAttrString(_pymessage, "eta", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
