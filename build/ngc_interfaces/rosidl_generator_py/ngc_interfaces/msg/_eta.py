# generated from rosidl_generator_py/resource/_idl.py.em
# with input from ngc_interfaces:msg/Eta.idl
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


class Metaclass_Eta(type):
    """Metaclass of message 'Eta'."""

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
                'ngc_interfaces.msg.Eta')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__eta
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__eta
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__eta
            cls._TYPE_SUPPORT = module.type_support_msg__msg__eta
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__eta

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class Eta(metaclass=Metaclass_Eta):
    """Message class 'Eta'."""

    __slots__ = [
        '_lat',
        '_lon',
        '_z',
        '_phi',
        '_theta',
        '_psi',
        '_check_fields',
    ]

    _fields_and_field_types = {
        'lat': 'float',
        'lon': 'float',
        'z': 'float',
        'phi': 'float',
        'theta': 'float',
        'psi': 'float',
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
        self.lat = kwargs.get('lat', float())
        self.lon = kwargs.get('lon', float())
        self.z = kwargs.get('z', float())
        self.phi = kwargs.get('phi', float())
        self.theta = kwargs.get('theta', float())
        self.psi = kwargs.get('psi', float())

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
        if self.lat != other.lat:
            return False
        if self.lon != other.lon:
            return False
        if self.z != other.z:
            return False
        if self.phi != other.phi:
            return False
        if self.theta != other.theta:
            return False
        if self.psi != other.psi:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def lat(self):
        """Message field 'lat'."""
        return self._lat

    @lat.setter
    def lat(self, value):
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'lat' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'lat' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._lat = value

    @builtins.property
    def lon(self):
        """Message field 'lon'."""
        return self._lon

    @lon.setter
    def lon(self, value):
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'lon' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'lon' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._lon = value

    @builtins.property
    def z(self):
        """Message field 'z'."""
        return self._z

    @z.setter
    def z(self, value):
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'z' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'z' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._z = value

    @builtins.property
    def phi(self):
        """Message field 'phi'."""
        return self._phi

    @phi.setter
    def phi(self, value):
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'phi' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'phi' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._phi = value

    @builtins.property
    def theta(self):
        """Message field 'theta'."""
        return self._theta

    @theta.setter
    def theta(self, value):
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'theta' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'theta' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._theta = value

    @builtins.property
    def psi(self):
        """Message field 'psi'."""
        return self._psi

    @psi.setter
    def psi(self, value):
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'psi' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'psi' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._psi = value
