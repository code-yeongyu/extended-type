from typing import Any

from pydantic import BaseConfig, BaseModel

from extended_type.extended_type_validator import ExtendedTypeValidator

validator = ExtendedTypeValidator()


class Validatable(BaseModel):
    class Config(BaseConfig):
        arbitrary_types_allowed = True  # for pydantic to allow extended types

    def __init__(
        self,
        *args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        for field_name, annotation in self.__annotations__.items():
            validator.validate_field(field_name, annotation, getattr(self, field_name))

    def __setattr__(self, name: str, value: Any):
        if name in self.__annotations__:
            validator.validate_field(name, self.__annotations__[name], value)
        super().__setattr__(name, value)
