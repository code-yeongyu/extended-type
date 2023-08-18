from __future__ import annotations

from typing import Any, Generic, TypeVar, cast

from typing_extensions import get_args

T = TypeVar("T", bound=str)


class ContainsStrType(str, Generic[T]):
    @staticmethod
    def extract_substring(annotation: type[Any]) -> str:
        # extracts ContainsStr[typing.Literal[SUBSTRING]], <class 'str'>
        union_args = cast(tuple[str], get_args(annotation))

        # extracts typing.Literal[SUBSTRING]
        extended_str_args = get_args(union_args[0])

        # extracts (SUBSTRING,)
        literal_substring = get_args(extended_str_args[0])

        # extracts SUBSTRING
        substring = literal_substring[0]
        return substring

    @staticmethod
    def validate(substring: str, value: str) -> str:
        if substring not in value:
            raise ValueError(f"`{value}` does not contain `{substring}`")
        return value


SUBSTRING = TypeVar("SUBSTRING", bound=str)
ContainsStr = ContainsStrType[SUBSTRING] | str
