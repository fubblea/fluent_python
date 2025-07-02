from dataclasses import InitVar, dataclass


@dataclass(frozen=True)
class Point:
    x: float
    y: float


def frozen_point():
    """Return a frozen copy of the given Point.

    >>> frozen_point()
    Error: cannot assign to field 'x'
    """
    p = Point(1.0, 2.0)

    try:
        p.x = 3.0  # type: ignore : This will raise an error since the dataclass is frozen
    except AttributeError as e:
        print(f"Error: {e}")


@dataclass
class Person:
    name: str
    age: int = 0

    def __post_init__(self):
        if self.age < 0:
            raise ValueError("Age cannot be negative")


def post_init():
    """Post init validation.

    >>> post_init()
    Person(name='Alice', age=30)
    Error: Age cannot be negative
    """
    p = Person(name="Alice", age=30)
    print(p)

    try:
        _ = Person(name="Bob", age=-5)  # This will raise an error
    except ValueError as e:
        print(f"Error: {e}")


@dataclass(order=True)
class Circle:
    radius: float


def dataclass_ordering():
    """Demonstrate ordering with dataclasses.

    >>> dataclass_ordering()
    Circle(radius=5.0)
    Circle(radius=10.0)
    Circle(radius=5.0) < Circle(radius=10.0): True
    """
    c1 = Circle(radius=5.0)
    c2 = Circle(radius=10.0)

    print(c1)
    print(c2)

    print(f"{c1} < {c2}: {c1 < c2}")


@dataclass
class C:
    i: int
    j: int
    lookup: InitVar[dict | None] = None  # These are not stored in the instance

    def __post_init__(self, lookup: dict | None = None):
        if lookup is not None:
            self.j = lookup.get(self.i, self.j)


def dataclass_with_initvar():
    """Demonstrate InitVar usage in dataclasses.

    >>> dataclass_with_initvar()
    C(i=1, j=10)
    C(i=2, j=20)
    """
    lookup = {1: 10, 2: 20}
    c1 = C(i=1, j=5, lookup=lookup)
    c2 = C(i=2, j=15, lookup=lookup)

    print(c1)
    print(c2)
