from __future__ import annotations

from typing import Any, Generic, TypeVar, cast

from typing_extensions import get_args

T = TypeVar("T", bound=str)


class PrefixStrType(str, Generic[T]):
    @staticmethod
    def extract_prefix(annotation: type[Any]) -> str:
        # extracts PrefixStr[typing.Literal[PREFIX]], <class 'str'>
        union_args = cast(tuple[str], get_args(annotation))

        # extracts typing.Literal[PREFIX]
        extended_str_args = get_args(union_args[0])

        # extracts (PREFIX,)
        literal_prefix = get_args(extended_str_args[0])

        # extracts PREFIX
        prefix = literal_prefix[0]
        return prefix

    @staticmethod
    def validate(prefix: str, value: str) -> str:
        if not value.startswith(prefix):
            raise ValueError(f"`{value}` does not start with `{prefix}`")
        return value


PREFIX = TypeVar("PREFIX", bound=str)
PrefixStr = PrefixStrType[PREFIX] | str
