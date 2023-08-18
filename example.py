from typing import Literal

from extended_type import RegexStr, Validatable
from extended_type.range_int import RangeInt


class School(Validatable):
    school_code: RegexStr[Literal["^school.*$"]]
    school_name: str
    teacher_count: RangeInt[Literal[0], Literal[10]]


school = School(school_code="school_1", school_name="School 1", teacher_count=0)
school = School(
    school_code="scho", school_name="School 1", teacher_count=0
)  # it will raise ValueError
for i in range(20):
    school.teacher_count = i  # when i = 11, it will raise ValueError
