from dataclasses import dataclass

METRO_AREAS = [
    ("Tokyo", "JP", 36.933, (35.689722, 139.691667)),
    ("Dehli NCR", "IN", 21.935, (28.613889, 77.208889)),
    ("Mexico City", "MX", 20.142, (19.433333, -99.133333)),
    ("New York-Newark", "US", 20.104, (40.808611, -74.020386)),
    ("Sao Paulo", "BR", 19.649, (-23.547778, -46.635833)),
]


def unpack_tuple():
    """Unpack tuple

    >>> unpack_tuple()
                    | latitude  | longitude
    Tokyo           | 35.689722 | 139.691667
    Dehli NCR       | 28.613889 | 77.208889
    Mexico City     | 19.433333 | -99.133333
    New York-Newark | 40.808611 | -74.020386
    Sao Paulo       | -23.547778 | -46.635833
    """

    print(f"{"":15} | {"latitude":9} | {"longitude":9}")
    for city, _, _, (lat, long) in METRO_AREAS:
        print(f"{city:15} | {lat:9} | {long:9}")


def match_case():
    """Match case

    >>> match_case()
    Default case
    Dehli NCR has long > 0
    Mexico City has ting < 21
    New York-Newark has ting < 21
    Sao Paulo has lat < 0, long < 0 with extras: ['BR', 19.649]
    """

    for record in METRO_AREAS:
        match record:
            # Optional guards with skip using *_
            case [city, *_, (_, long)] if (long > 0 and city != "Tokyo"):
                print(f"{city} has long > 0")

            # Optional guards with extras
            case [city, *extras, (lat, long)] if (long < 0 and lat < 0):
                print(f"{city} has lat < 0, long < 0 with extras: {extras}")

            # Can use type matching using "constructor" syntax
            case [str(city), *_, float(ting), _] if ting < 21:
                print(f"{city} has ting < 21")

            case _:
                print("Default case")


def with_dicts(record: dict) -> list:
    """Function that gets the creators from a record

    Parameters
    ----------
    record : dict
        Input data

    Returns
    -------
    list
        Creators

    >>> with_dicts(dict(api=1, author="Ajay Anand", type="book"))
    ['Ajay Anand']

    Order does not matter:
    >>> from typing import OrderedDict
    >>> with_dicts(OrderedDict(api=1, author="Ajay Anand", type="book"))
    ['Ajay Anand']

    >>> with_dicts(dict(api=2, authors="Anand Holden".split(), type="book", pages=200))
    ['Anand', 'Holden']

    >>> with_dicts(dict(api=3, authors="Anand Holden".split(), type="book", pages=200))
    Other details: {'pages': 200}
    ['Anand', 'Holden']

    """

    match record:
        case {"type": "book", "api": 3, "authors": [*names], **details}:
            print(f"Other details: {details}")
            return names

        case {"type": "book", "api": 2, "authors": [*names]}:
            return names

        case {"type": "book", "api": 1, "author": name}:
            return [name]

        case {"type": "book"}:
            # The "!r" means use the __repr__() instead of the __str__()
            raise ValueError(f"Invalid record: {record!r}")

        case _:
            raise ValueError(f"Unable to parse record: {record!r}")


@dataclass
class City:
    continent: str
    country: str


def match_case_with_class():
    """Match case with class

    >>> match_case_with_class()
    Asia: ['JP', 'IN']
    North America: ['MX', 'US']
    """

    asia = []
    north_america = []

    cities = [
        City(continent="Asia", country="JP"),
        City(continent="Asia", country="IN"),
        City(continent="North America", country="MX"),
        City(continent="North America", country="US"),
    ]

    for city in cities:
        match city:
            case City(continent="Asia", country=country):
                asia.append(country)

            case City(continent="North America", country=country):
                north_america.append(country)

            case _:
                print(f"Unknown city: {city}")

    print(f"Asia: {asia}")
    print(f"North America: {north_america}")
