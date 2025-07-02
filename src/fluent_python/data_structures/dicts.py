from collections import UserDict, defaultdict

DIAL_CODES = [
    (86, "China"),
    (91, "India"),
    (1, "United States"),
    (62, "Indonesia"),
    (55, "Brazil"),
    (92, "Pakistan"),
    (880, "Bangladesh"),
    (234, "Nigeria"),
    (7, "Russia"),
    (81, "Japan"),
]


def dict_comp():
    """Dictionary comp example with guard

    >>> dict_comp()
    {1: 'UNITED STATES', 7: 'RUSSIA'}
    """
    return {code: country.upper() for (code, country) in DIAL_CODES if code < 50}


def merge_maps():
    """Merge mappings example

    >>> merge_maps()
    {'a': 8, 'b': 4, 'c': 6}
    {'a': 8, 'b': 4, 'c': 6}
    """

    d1 = {"a": 1, "b": 3}
    d2 = {"a": 8, "b": 4, "c": 6}

    # d2 will over-write
    print(d1 | d2)

    # This is inplace
    d1 |= d2
    print(d1)


def get_with_default():
    """Get with default

    >>> get_with_default()
    5
    5
    {'a': 2, 'b': 3, 'c': 5}
    """

    d = {"a": 2, "b": 3}

    print(d.get("c", 5))

    # Can use set default to add inplace

    d.setdefault("b", 5)  # This will do nothing

    # setdefault returns the value to. Can be used instead of get if mutating
    print(d.setdefault("c", 5))

    print(d)


def default_dicts():
    """Default dict example

    >>> default_dicts()
    defaultdict(<class 'int'>, {'a': 2, 'b': 3})
    2
    0
    defaultdict(<class 'int'>, {'a': 2, 'b': 3, 'c': 0})
    False
    None
    """

    dd = defaultdict(int)
    dd |= {"a": 2, "b": 3}

    print(dd)
    print(dd["a"])

    # This updates in-place
    print(dd["c"])
    print(dd)

    # The default value will only be created when __getitem__ is called
    print("d" in dd)
    print(dd.get("d"))


# It is better to inherit from collecitons.UserDict than dict
class CustomDict(UserDict):
    """
    CustomDict is a subclass of UserDict that automatically assigns the value "potato"
    to any missing key accessed. When a missing key is accessed, it is added to the
    dictionary with the value "potato" and "potato" is returned.
    Methods
    -------
    __missing__(key):
        Handles missing keys by setting their value to "potato" and returning "potato".
    """

    def __missing__(self, key):
        self[key] = "potato"
        return "potato"


def custom_missing():
    """Custom __missing__ dict example

    >>> custom_missing()
    {'a': 2, 'b': 3}
    2
    potato
    {'a': 2, 'b': 3, 'c': 'potato'}
    """

    dd = CustomDict({"a": 2, "b": 3})

    print(dd)
    print(dd["a"])

    # This calls __missing__
    print(dd["c"])
    print(dd)
