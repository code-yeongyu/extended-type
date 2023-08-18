from typing import Type


def class_wrapper(cls: Type, target: Type) -> Type:
    class NewClass(cls, target):
        def __init__(self, *args, **kwargs):
            cls.__init__(self, *args, **kwargs)
            target.__init__(self, *args, **kwargs)

    NewClass.__name__ = cls.__name__
    return NewClass
