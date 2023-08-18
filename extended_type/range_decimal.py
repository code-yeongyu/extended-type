from __future__ import annotations

from decimal import Decimal
from types import NoneType
from typing import Any, Generic, TypeVar

from typing_extensions import get_args

from extended_type.range_numeric import RangeNumericBase

MIN_DECIMAL = TypeVar("MIN_DECIMAL", bound=str | int | None)
MAX_DECIMAL = TypeVar("MAX_DECIMAL", bound=str | int | None)


class RangeDecimalType(Decimal, Generic[MIN_DECIMAL, MAX_DECIMAL], RangeNumericBase):
    @staticmethod
    def extract_range(
        annotation: type[Any],
    ) -> tuple[Decimal | None, Decimal | None]:
        def get_number(literal_arg: type[Any]) -> Decimal | None:
            if literal_arg is NoneType:
                return None

            arg = get_args(literal_arg)[0]
            if arg is None:
                return None
            return Decimal(arg)  # extracts MIN_DECIMAL or MAX_DECIMAL

        # extracts RangeDecimalType[typing.Literal[MIN_DECIMAL], typing.Literal[MAX_DECIMAL]], <class 'Decimal'>
        union_args = get_args(annotation)

        # extracts typing.Literal[MIN_DECIMAL], typing.Literal[MAX_DECIMAL]
        range_literal_args = get_args(union_args[0])

        # extracts (MIN_DECIMAL,), (MAX_DECIMAL,)
        min_value = get_number(range_literal_args[0])
        max_value = get_number(range_literal_args[1])
        return min_value, max_value


RangeDecimal = RangeDecimalType[MIN_DECIMAL, MAX_DECIMAL] | Decimal
