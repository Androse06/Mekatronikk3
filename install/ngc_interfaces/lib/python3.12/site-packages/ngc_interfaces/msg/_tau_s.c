// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from ngc_interfaces:msg/Tau.idl
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
#include "ngc_interfaces/msg/detail/tau__struct.h"
#include "ngc_interfaces/msg/detail/tau__functions.h"


ROSIDL_GENERATOR_C_EXPORT
bool ngc_interfaces__msg__tau__convert_from_py(PyObject * _pymsg, void * _ros_message)
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
    assert(strncmp("ngc_interfaces.msg._tau.Tau", full_classname_dest, 27) == 0);
  }
  ngc_interfaces__msg__Tau * ros_message = _ros_message;
  {  // surge_x
    PyObject * field = PyObject_GetAttrString(_pymsg, "surge_x");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->surge_x = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // sway_y
    PyObject * field = PyObject_GetAttrString(_pymsg, "sway_y");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->sway_y = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // heave_z
    PyObject * field = PyObject_GetAttrString(_pymsg, "heave_z");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->heave_z = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // roll_k
    PyObject * field = PyObject_GetAttrString(_pymsg, "roll_k");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->roll_k = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // pitch_m
    PyObject * field = PyObject_GetAttrString(_pymsg, "pitch_m");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->pitch_m = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // yaw_n
    PyObject * field = PyObject_GetAttrString(_pymsg, "yaw_n");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->yaw_n = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * ngc_interfaces__msg__tau__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of Tau */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("ngc_interfaces.msg._tau");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "Tau");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  ngc_interfaces__msg__Tau * ros_message = (ngc_interfaces__msg__Tau *)raw_ros_message;
  {  // surge_x
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->surge_x);
    {
      int rc = PyObject_SetAttrString(_pymessage, "surge_x", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // sway_y
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->sway_y);
    {
      int rc = PyObject_SetAttrString(_pymessage, "sway_y", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // heave_z
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->heave_z);
    {
      int rc = PyObject_SetAttrString(_pymessage, "heave_z", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // roll_k
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->roll_k);
    {
      int rc = PyObject_SetAttrString(_pymessage, "roll_k", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // pitch_m
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->pitch_m);
    {
      int rc = PyObject_SetAttrString(_pymessage, "pitch_m", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // yaw_n
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->yaw_n);
    {
      int rc = PyObject_SetAttrString(_pymessage, "yaw_n", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
