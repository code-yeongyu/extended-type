from typing import Any, Type

from extended_type.extended_type_validator import ExtendedTypeValidator
from extended_type.utils import class_wrapper

validator = ExtendedTypeValidator()


class TypeExtended:
    def __init__(
        self,
        *args,
        **kwargs,
    ):
        self._make_pydantic_compatible()
        for field_name, annotation in self.__annotations__.items():
            validator.validate_field(field_name, annotation, getattr(self, field_name))

    def __setattr__(self, name: str, value: Any):
        if name in self.__annotations__:
            validator.validate_field(name, self.__annotations__[name], value)
        super().__setattr__(name, value)

    def _make_pydantic_compatible(self):
        if hasattr(self, "Config"):
            self.Config.arbitrary_types_allowed = True


def type_extended(cls: Type):
    return class_wrapper(cls, TypeExtended)
