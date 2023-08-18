from typing import Type


def class_wrapper(cls: Type, target: Type) -> Type:
    class WrappedTypeExtendedClass(cls, target):
        def __init__(self, *args, **kwargs):
            cls.__init__(self, *args, **kwargs)
            target.__init__(self, *args, **kwargs)

    WrappedTypeExtendedClass.__name__ = cls.__name__
    return WrappedTypeExtendedClass
