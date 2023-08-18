from __future__ import annotations

import re
from typing import Any, Generic, Literal, TypeVar, cast

from typing_extensions import get_args

T = TypeVar("T", bound=str)


class RegexStrType(str, Generic[T]):
    @staticmethod
    def extract_pattern(annotation: type[Any]) -> str:
        # extracts RegexStr[typing.Literal[PATTERN]], <class 'str'>
        union_args = cast(tuple[str], get_args(annotation))

        # extracts typing.Literal[PATTERN]
        extended_str_args = get_args(union_args[0])

        # extracts (PATTERN,)
        literal_pattern = get_args(extended_str_args[0])

        # extracts PATTERN
        pattern = literal_pattern[0]
        return pattern

    @staticmethod
    def validate(pattern: str, value: str) -> str:
        if not re.match(pattern, value):
            raise ValueError(f"`{value}` does not match `{pattern}`")
        return value


PATTERN = TypeVar("PATTERN", bound=str)
RegexStr = RegexStrType[PATTERN] | str


EmailStr = (
    RegexStrType[Literal["^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$"]] | str
)
