# generated from rosidl_generator_py/resource/_idl.py.em
# with input from ngc_interfaces:msg/NuDot.idl
# generated code does not contain a copyright notice

# This is being done at the module level and not on the instance level to avoid looking
# for the same variable multiple times on each instance. This variable is not supposed to
# change during runtime so it makes sense to only look for it once.
from os import getenv

ros_python_check_fields = getenv('ROS_PYTHON_CHECK_FIELDS', default='')


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_NuDot(type):
    """Metaclass of message 'NuDot'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('ngc_interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'ngc_interfaces.msg.NuDot')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__nu_dot
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__nu_dot
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__nu_dot
            cls._TYPE_SUPPORT = module.type_support_msg__msg__nu_dot
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__nu_dot

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class NuDot(metaclass=Metaclass_NuDot):
    """Message class 'NuDot'."""

    __slots__ = [
        '_u_dot',
        '_v_dot',
        '_w_dot',
        '_p_dot',
        '_q_dot',
        '_r_dot',
        '_check_fields',
    ]

    _fields_and_field_types = {
        'u_dot': 'float',
        'v_dot': 'float',
        'w_dot': 'float',
        'p_dot': 'float',
        'q_dot': 'float',
        'r_dot': 'float',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        if 'check_fields' in kwargs:
            self._check_fields = kwargs['check_fields']
        else:
            self._check_fields = ros_python_check_fields == '1'
        if self._check_fields:
            assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
                'Invalid arguments passed to constructor: %s' % \
                ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.u_dot = kwargs.get('u_dot', float())
        self.v_dot = kwargs.get('v_dot', float())
        self.w_dot = kwargs.get('w_dot', float())
        self.p_dot = kwargs.get('p_dot', float())
        self.q_dot = kwargs.get('q_dot', float())
        self.r_dot = kwargs.get('r_dot', float())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.get_fields_and_field_types().keys(), self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    if self._check_fields:
                        assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.u_dot != other.u_dot:
            return False
        if self.v_dot != other.v_dot:
            return False
        if self.w_dot != other.w_dot:
            return False
        if self.p_dot != other.p_dot:
            return False
        if self.q_dot != other.q_dot:
            return False
        if self.r_dot != other.r_dot:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def u_dot(self):
        """Message field 'u_dot'."""
        return self._u_dot

    @u_dot.setter
    def u_dot(self, value):
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'u_dot' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'u_dot' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._u_dot = value

    @builtins.property
    def v_dot(self):
        """Message field 'v_dot'."""
        return self._v_dot

    @v_dot.setter
    def v_dot(self, value):
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'v_dot' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'v_dot' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._v_dot = value

    @builtins.property
    def w_dot(self):
        """Message field 'w_dot'."""
        return self._w_dot

    @w_dot.setter
    def w_dot(self, value):
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'w_dot' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'w_dot' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._w_dot = value

    @builtins.property
    def p_dot(self):
        """Message field 'p_dot'."""
        return self._p_dot

    @p_dot.setter
    def p_dot(self, value):
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'p_dot' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'p_dot' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._p_dot = value

    @builtins.property
    def q_dot(self):
        """Message field 'q_dot'."""
        return self._q_dot

    @q_dot.setter
    def q_dot(self, value):
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'q_dot' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'q_dot' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._q_dot = value

    @builtins.property
    def r_dot(self):
        """Message field 'r_dot'."""
        return self._r_dot

    @r_dot.setter
    def r_dot(self, value):
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'r_dot' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'r_dot' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._r_dot = value
