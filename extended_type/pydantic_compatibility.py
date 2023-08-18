# Try to import pydantic and set a flag based on its availability

from typing import Type

from extended_type.utils import class_wrapper

PYDANTIC_AVAILABLE = False

try:
    from pydantic import BaseConfig, BaseModel

    from .type_extended import TypeExtended

    class TypeExtendedBaseModel(BaseModel, TypeExtended):
        class Config(BaseConfig):
            arbitrary_types_allowed = True

        def __init__(self, *args, **kwargs):
            # todo: conversion layer of pydantic.Field using annotation
            super().__init__(*args, **kwargs)

    def type_extended_base_model(cls: Type):
        return class_wrapper(cls, TypeExtendedBaseModel)

    PYDANTIC_AVAILABLE = True

except ImportError:
    pass
