// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from ngc_interfaces:msg/Wind.idl
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
#include "ngc_interfaces/msg/detail/wind__struct.h"
#include "ngc_interfaces/msg/detail/wind__functions.h"


ROSIDL_GENERATOR_C_EXPORT
bool ngc_interfaces__msg__wind__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[30];
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
    assert(strncmp("ngc_interfaces.msg._wind.Wind", full_classname_dest, 29) == 0);
  }
  ngc_interfaces__msg__Wind * ros_message = _ros_message;
  {  // direction_relative_deg
    PyObject * field = PyObject_GetAttrString(_pymsg, "direction_relative_deg");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->direction_relative_deg = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // magnitude_ms
    PyObject * field = PyObject_GetAttrString(_pymsg, "magnitude_ms");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->magnitude_ms = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * ngc_interfaces__msg__wind__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of Wind */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("ngc_interfaces.msg._wind");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "Wind");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  ngc_interfaces__msg__Wind * ros_message = (ngc_interfaces__msg__Wind *)raw_ros_message;
  {  // direction_relative_deg
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->direction_relative_deg);
    {
      int rc = PyObject_SetAttrString(_pymessage, "direction_relative_deg", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // magnitude_ms
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->magnitude_ms);
    {
      int rc = PyObject_SetAttrString(_pymessage, "magnitude_ms", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
