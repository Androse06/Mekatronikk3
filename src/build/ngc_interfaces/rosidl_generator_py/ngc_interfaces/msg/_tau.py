# generated from rosidl_generator_py/resource/_idl.py.em
# with input from ngc_interfaces:msg/Tau.idl
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


class Metaclass_Tau(type):
    """Metaclass of message 'Tau'."""

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
                'ngc_interfaces.msg.Tau')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__tau
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__tau
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__tau
            cls._TYPE_SUPPORT = module.type_support_msg__msg__tau
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__tau

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class Tau(metaclass=Metaclass_Tau):
    """Message class 'Tau'."""

    __slots__ = [
        '_surge_x',
        '_surge_y',
        '_sway_y',
        '_heave_z',
        '_roll_k',
        '_pitch_m',
        '_yaw_n',
        '_check_fields',
    ]

    _fields_and_field_types = {
        'surge_x': 'float',
        'surge_y': 'float',
        'sway_y': 'float',
        'heave_z': 'float',
        'roll_k': 'float',
        'pitch_m': 'float',
        'yaw_n': 'float',
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
        self.surge_x = kwargs.get('surge_x', float())
        self.surge_y = kwargs.get('surge_y', float())
        self.sway_y = kwargs.get('sway_y', float())
        self.heave_z = kwargs.get('heave_z', float())
        self.roll_k = kwargs.get('roll_k', float())
        self.pitch_m = kwargs.get('pitch_m', float())
        self.yaw_n = kwargs.get('yaw_n', float())

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
        if self.surge_x != other.surge_x:
            return False
        if self.surge_y != other.surge_y:
            return False
        if self.sway_y != other.sway_y:
            return False
        if self.heave_z != other.heave_z:
            return False
        if self.roll_k != other.roll_k:
            return False
        if self.pitch_m != other.pitch_m:
            return False
        if self.yaw_n != other.yaw_n:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def surge_x(self):
        """Message field 'surge_x'."""
        return self._surge_x

    @surge_x.setter
    def surge_x(self, value):
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'surge_x' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'surge_x' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._surge_x = value

    @builtins.property
    def surge_y(self):
        """Message field 'surge_y'."""
        return self._surge_y

    @surge_y.setter
    def surge_y(self, value):
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'surge_y' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'surge_y' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._surge_y = value

    @builtins.property
    def sway_y(self):
        """Message field 'sway_y'."""
        return self._sway_y

    @sway_y.setter
    def sway_y(self, value):
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'sway_y' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'sway_y' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._sway_y = value

    @builtins.property
    def heave_z(self):
        """Message field 'heave_z'."""
        return self._heave_z

    @heave_z.setter
    def heave_z(self, value):
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'heave_z' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'heave_z' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._heave_z = value

    @builtins.property
    def roll_k(self):
        """Message field 'roll_k'."""
        return self._roll_k

    @roll_k.setter
    def roll_k(self, value):
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'roll_k' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'roll_k' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._roll_k = value

    @builtins.property
    def pitch_m(self):
        """Message field 'pitch_m'."""
        return self._pitch_m

    @pitch_m.setter
    def pitch_m(self, value):
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'pitch_m' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'pitch_m' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._pitch_m = value

    @builtins.property
    def yaw_n(self):
        """Message field 'yaw_n'."""
        return self._yaw_n

    @yaw_n.setter
    def yaw_n(self, value):
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'yaw_n' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'yaw_n' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._yaw_n = value
