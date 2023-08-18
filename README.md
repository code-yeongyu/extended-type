# extended-type

Boost Python's type hinting with extended-types: regex and range validations seamlessly integrated with Pydantic.

This is an experimental collection of code snippets that work as intended, but it's not packaged for distribution yet.

```python
from typing import Literal
from extended_type import RegexStr, Validatable

class School(Validatable):
    school_code: RegexStr[Literal["^school.*$"]]
    school_name: str
    age: RangeInt[Literal[10], Literal[20]]

school = School(school_code="school_1", school_name="School 1", age=15) # okay
school = School(school_code="sch", school_name="School 1", age=10) # ValueError: 'sch' does not match regex pattern '^school.*$'
school = School(school_code="school_1", school_name="School 1", age=21) # ValueError: 21 is not in range [10, 20]
school.school_code = "sch" # ValueError: 'sch' does not match regex pattern '^school.*$'
```

## Types Extended

### str

- `RegexStr`: Easily validate string attributes with regex patterns.

```python
from typing import Literal
from extended_type import RegexStr, Validatable

class School(Validatable):
    school_code: RegexStr[Literal["^school.*$"]]
    school_name: str

school = School(school_code="school_1", school_name="School 1")
school = School(school_code="scho", school_name="School 1") # ValueError: 'scho' does not match regex pattern '^school.*$'
```

### Numeric

- `RangeInt`: Set boundaries for integer attributes.

```python
from typing import Literal
from extended_type.range_int import RangeInt, Validatable

class Student(Validatable):
    age: RangeInt[Literal[10], Literal[20]]

student = Student(age=15)
student = Student(age=9) # ValueError: 9 is not in range [10, 20]
student = Student(age=21) # ValueError: 21 is not in range [10, 20]
```

- `RangeFloat`: Set boundaries for float attributes.

```python
from typing import Literal
from extended_type.range_float import RangeFloat, Validatable

class Product(Validatable):
    weight: RangeFloat[Literal['0.5'], Literal['5.0']]
    height: RangeFloat[Literal[1], Literal[5]]

product = Product(weight=2.5, height=2.5)
product = Product(weight=0.4, height=3) # ValueError: 0.4 is not in range [0.5, 5.0]
product = Product(weight=2.5, height=7) # ValueError: 7 is not in range [1.0, 5.0]
```

- `RangeDecimal`: Set boundaries for decimal attributes.

```python
from typing import Literal
from extended_type.range_decimal import RangeDecimal, Validatable

class Transaction(Validatable):
    amount: RangeDecimal[Literal["0.01"], Literal["1000.00"]]
    amount2: RangeDecimal[Literal[1], Literal[10]]

transaction = Transaction(amount=Decimal("150.75"), amount2=Decimal("5.0"))
transaction = Transaction(amount=Decimal("0.005"), amount2=Decimal("5.0")) # ValueError: 0.005 is not in range [0.01, 1000.00]
transaction = Transaction(amount=Decimal("150.75"), amount2=Decimal("15")) # ValueError: 15 is not in range [1, 10]
```

### ETC

... More types will be added soon.
Your suggestions are welcome! 🎉

## To Do

- [ ] Add Tests
- [ ] Add CI/CD
- [ ] Add PyPi package
- [ ] Add more types (Suggestions are welcome! 🎉)
