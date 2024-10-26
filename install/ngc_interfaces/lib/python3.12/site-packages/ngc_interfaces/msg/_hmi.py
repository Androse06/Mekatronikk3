# generated from rosidl_generator_py/resource/_idl.py.em
# with input from ngc_interfaces:msg/HMI.idl
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


class Metaclass_HMI(type):
    """Metaclass of message 'HMI'."""

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
                'ngc_interfaces.msg.HMI')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__hmi
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__hmi
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__hmi
            cls._TYPE_SUPPORT = module.type_support_msg__msg__hmi
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__hmi

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class HMI(metaclass=Metaclass_HMI):
    """Message class 'HMI'."""

    __slots__ = [
        '_mode',
        '_route',
        '_point',
        '_nu',
        '_eta',
        '_check_fields',
    ]

    _fields_and_field_types = {
        'mode': 'int32',
        'route': 'boolean',
        'point': 'boolean',
        'nu': 'float',
        'eta': 'float',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
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
        self.mode = kwargs.get('mode', int())
        self.route = kwargs.get('route', bool())
        self.point = kwargs.get('point', bool())
        self.nu = kwargs.get('nu', float())
        self.eta = kwargs.get('eta', float())

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
        if self.mode != other.mode:
            return False
        if self.route != other.route:
            return False
        if self.point != other.point:
            return False
        if self.nu != other.nu:
            return False
        if self.eta != other.eta:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def mode(self):
        """Message field 'mode'."""
        return self._mode

    @mode.setter
    def mode(self, value):
        if self._check_fields:
            assert \
                isinstance(value, int), \
                "The 'mode' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'mode' field must be an integer in [-2147483648, 2147483647]"
        self._mode = value

    @builtins.property
    def route(self):
        """Message field 'route'."""
        return self._route

    @route.setter
    def route(self, value):
        if self._check_fields:
            assert \
                isinstance(value, bool), \
                "The 'route' field must be of type 'bool'"
        self._route = value

    @builtins.property
    def point(self):
        """Message field 'point'."""
        return self._point

    @point.setter
    def point(self, value):
        if self._check_fields:
            assert \
                isinstance(value, bool), \
                "The 'point' field must be of type 'bool'"
        self._point = value

    @builtins.property
    def nu(self):
        """Message field 'nu'."""
        return self._nu

    @nu.setter
    def nu(self, value):
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'nu' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'nu' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._nu = value

    @builtins.property
    def eta(self):
        """Message field 'eta'."""
        return self._eta

    @eta.setter
    def eta(self, value):
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'eta' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'eta' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._eta = value
