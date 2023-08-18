from __future__ import annotations

from typing import Any, Generic, TypeVar, cast

from typing_extensions import get_args

T = TypeVar("T", bound=str)


class SuffixStrType(str, Generic[T]):
    @staticmethod
    def extract_suffix(annotation: type[Any]) -> str:
        # extracts SuffixStr[typing.Literal[SUFFIX]], <class 'str'>
        union_args = cast(tuple[str], get_args(annotation))

        # extracts typing.Literal[SUFFIX]
        extended_str_args = get_args(union_args[0])

        # extracts (SUFFIX,)
        literal_suffix = get_args(extended_str_args[0])

        # extracts SUFFIX
        suffix = literal_suffix[0]
        return suffix

    @staticmethod
    def validate(suffix: str, value: str) -> str:
        if not value.endswith(suffix):
            raise ValueError(f"`{value}` does not end with `{suffix}`")
        return value


SUFFIX = TypeVar("SUFFIX", bound=str)
SuffixStr = SuffixStrType[SUFFIX] | str
