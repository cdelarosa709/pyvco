from zope.interface import implements
from interfaces import ITypedValue

class TypedValue(object):
    implements(ITypedValue)

    def __init__(self, type, value):
        """Build a typed value

        :param type: type of the value
        :param value: string representation of the value
        """
        self._type = type
        self._value = value

    def type(self):
        return self._type

    def value(self):
        return self._value