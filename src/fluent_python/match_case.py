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
