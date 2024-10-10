# generated from rosidl_generator_py/resource/_idl.py.em
# with input from ngc_interfaces:msg/ThrusterSignals.idl
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


class Metaclass_ThrusterSignals(type):
    """Metaclass of message 'ThrusterSignals'."""

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
                'ngc_interfaces.msg.ThrusterSignals')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__thruster_signals
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__thruster_signals
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__thruster_signals
            cls._TYPE_SUPPORT = module.type_support_msg__msg__thruster_signals
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__thruster_signals

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class ThrusterSignals(metaclass=Metaclass_ThrusterSignals):
    """Message class 'ThrusterSignals'."""

    __slots__ = [
        '_thruster_id',
        '_rps',
        '_pitch',
        '_azimuth_deg',
        '_active',
        '_error',
        '_check_fields',
    ]

    _fields_and_field_types = {
        'thruster_id': 'int32',
        'rps': 'double',
        'pitch': 'double',
        'azimuth_deg': 'double',
        'active': 'boolean',
        'error': 'boolean',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
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
        self.thruster_id = kwargs.get('thruster_id', int())
        self.rps = kwargs.get('rps', float())
        self.pitch = kwargs.get('pitch', float())
        self.azimuth_deg = kwargs.get('azimuth_deg', float())
        self.active = kwargs.get('active', bool())
        self.error = kwargs.get('error', bool())

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
        if self.thruster_id != other.thruster_id:
            return False
        if self.rps != other.rps:
            return False
        if self.pitch != other.pitch:
            return False
        if self.azimuth_deg != other.azimuth_deg:
            return False
        if self.active != other.active:
            return False
        if self.error != other.error:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def thruster_id(self):
        """Message field 'thruster_id'."""
        return self._thruster_id

    @thruster_id.setter
    def thruster_id(self, value):
        if self._check_fields:
            assert \
                isinstance(value, int), \
                "The 'thruster_id' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'thruster_id' field must be an integer in [-2147483648, 2147483647]"
        self._thruster_id = value

    @builtins.property
    def rps(self):
        """Message field 'rps'."""
        return self._rps

    @rps.setter
    def rps(self, value):
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'rps' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'rps' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._rps = value

    @builtins.property
    def pitch(self):
        """Message field 'pitch'."""
        return self._pitch

    @pitch.setter
    def pitch(self, value):
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'pitch' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'pitch' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._pitch = value

    @builtins.property
    def azimuth_deg(self):
        """Message field 'azimuth_deg'."""
        return self._azimuth_deg

    @azimuth_deg.setter
    def azimuth_deg(self, value):
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'azimuth_deg' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'azimuth_deg' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._azimuth_deg = value

    @builtins.property
    def active(self):
        """Message field 'active'."""
        return self._active

    @active.setter
    def active(self, value):
        if self._check_fields:
            assert \
                isinstance(value, bool), \
                "The 'active' field must be of type 'bool'"
        self._active = value

    @builtins.property
    def error(self):
        """Message field 'error'."""
        return self._error

    @error.setter
    def error(self, value):
        if self._check_fields:
            assert \
                isinstance(value, bool), \
                "The 'error' field must be of type 'bool'"
        self._error = value
