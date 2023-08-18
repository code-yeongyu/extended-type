from __future__ import annotations

from types import NoneType
from typing import Any, Generic, TypeVar

from typing_extensions import get_args

from extended_type.range_numeric import RangeNumericBase

MIN = TypeVar("MIN", bound=int | None)
MAX = TypeVar("MAX", bound=int | None)


class RangeIntType(int, Generic[MIN, MAX], RangeNumericBase):
    @staticmethod
    def extract_range(
        annotation: type[Any],
    ) -> tuple[int | None, int | None]:
        def get_number(literal_arg: type[Any]) -> int | None:
            if literal_arg is NoneType:
                return None
            arg = get_args(literal_arg)[0]
            return arg  # extracts MIN or MAX

        # extracts RangeIntType[typing.Literal[MIN], typing.Literal[MAX]], <class 'int'>
        union_args = get_args(annotation)

        # extracts typing.Literal[MIN], typing.Literal[MAX]
        range_literal_args = get_args(union_args[0])

        # extracts (MIN,), (MAX,)
        min_value = get_number(range_literal_args[0])
        max_value = get_number(range_literal_args[1])
        return min_value, max_value


RangeInt = RangeIntType[MIN, MAX] | int
