from typing import Any, Callable, Union, cast

from typing_extensions import get_args, get_origin

from extended_type.contains_str import ContainsStrType
from extended_type.prefix_str import PrefixStrType
from extended_type.range_decimal import RangeDecimalType
from extended_type.range_float import RangeFloatType
from extended_type.range_int import RangeIntType
from extended_type.range_numeric import NUMERIC_TYPE, RangeNumericBase
from extended_type.regex_str import RegexStrType
from extended_type.suffix_str import SuffixStrType


class ExtendedTypeValidator:
    validators: dict[type, Callable[[Any, type[Any]], None]]

    def __init__(
        self,
        validators: dict[type, Callable[[Any, type[Any]], None]] | None = None,
    ):
        self.validators = validators or {
            RegexStrType: self._validate_regex_str,
            PrefixStrType: self._validate_prefix_str,
            SuffixStrType: self._validate_suffix_str,
            ContainsStrType: self._validate_contains_str,
            RangeIntType: lambda value, annotation: self._validate_number(
                cast(RangeNumericBase, RangeIntType), value, annotation
            ),
            RangeFloatType: lambda value, annotation: self._validate_number(
                cast(RangeNumericBase, RangeFloatType), value, annotation
            ),
            RangeDecimalType: lambda value, annotation: self._validate_number(
                cast(RangeNumericBase, RangeDecimalType), value, annotation
            ),
        }

    def validate_field(self, field_name: str, annotation: type[Any], value: Any):
        if get_origin(annotation) is not Union:
            return

        extended_type = get_origin(get_args(annotation)[0])
        if extended_type not in self.validators:
            return

        try:
            self.validators[extended_type](value, annotation)
        except ValueError as e:
            raise ValueError(f"Field '{field_name}': {e}")

    def _validate_number(
        self,
        extended_type: RangeNumericBase,
        value: NUMERIC_TYPE,
        annotation: type[Any],
    ):
        min_value, max_value = extended_type.extract_range(annotation)
        extended_type.validate(min_value, max_value, value)  # type: ignore

    def _validate_regex_str(self, value: str, annotation: type[str]):
        pattern = RegexStrType.extract_pattern(annotation)
        RegexStrType.validate(pattern, value)

    def _validate_email_str(self, value: str, _annotation: type[str]):
        EMAIL_PATTERN = "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$"
        RegexStrType.validate(EMAIL_PATTERN, value)

    def _validate_prefix_str(self, value: str, annotation: type[str]):
        prefix = PrefixStrType.extract_prefix(annotation)
        PrefixStrType.validate(prefix, value)

    def _validate_suffix_str(self, value: str, annotation: type[str]):
        subfix = SuffixStrType.extract_suffix(annotation)
        SuffixStrType.validate(subfix, value)

    def _validate_contains_str(self, value: str, annotation: type[str]):
        subset = ContainsStrType.extract_substring(annotation)
        ContainsStrType.validate(subset, value)
