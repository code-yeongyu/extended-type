from __future__ import annotations

from types import NoneType
from typing import Any, Generic, TypeVar

from typing_extensions import get_args

from extended_type.range_numeric import RangeNumericBase

MIN_FLOAT = TypeVar("MIN_FLOAT", bound=str | int | None)
MAX_FLOAT = TypeVar("MAX_FLOAT", bound=str | int | None)


class RangeFloatType(float, Generic[MIN_FLOAT, MAX_FLOAT], RangeNumericBase):
    @staticmethod
    def extract_range(
        annotation: type[Any],
    ) -> tuple[float | None, float | None]:
        def get_number(literal_arg: type[Any]) -> float | None:
            if literal_arg is NoneType:
                return None
            arg = get_args(literal_arg)[0]
            return float(arg)  # extracts MIN_FLOAT or MAX_FLOAT

        # extracts RangeFloatType[typing.Literal[MIN_FLOAT], typing.Literal[MAX_FLOAT]], <class 'float'>
        union_args = get_args(annotation)

        # extracts typing.Literal[MIN_FLOAT], typing.Literal[MAX_FLOAT]
        range_literal_args = get_args(union_args[0])

        # extracts (MIN_FLOAT,), (MAX_FLOAT,)
        min_value = get_number(range_literal_args[0])
        max_value = get_number(range_literal_args[1])
        return min_value, max_value


RangeFloat = RangeFloatType[MIN_FLOAT, MAX_FLOAT] | float
