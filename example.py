from dataclasses import dataclass
from typing import Literal

from extended_type import RangeInt, RegexStr
from extended_type.type_extended import type_extended


@type_extended
@dataclass
class School:
    school_code: RegexStr[Literal["^school.*$"]]
    school_name: str
    teacher_count: RangeInt[Literal[0], Literal[10]]


school = School(school_code="sch1", school_name="School 11", teacher_count=0)

school.teacher_count = 12
print(school)
