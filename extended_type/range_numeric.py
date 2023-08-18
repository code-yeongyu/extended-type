from decimal import Decimal
from typing import Any

NUMERIC_TYPE = int | float | Decimal


class RangeNumericBase:
    @staticmethod
    def extract_range(
        annotation: type[Any],
    ) -> tuple[NUMERIC_TYPE | None, NUMERIC_TYPE | None]:
        raise NotImplementedError

    @staticmethod
    def validate(
        min_value: NUMERIC_TYPE | None,
        max_value: NUMERIC_TYPE | None,
        value: NUMERIC_TYPE,
    ) -> NUMERIC_TYPE:
        if min_value is not None and value < min_value:
            raise ValueError(f"Value {value} is less than {min_value}")
        if max_value is not None and value > max_value:
            raise ValueError(f"Value {value} is greater than {max_value}")
        return value
