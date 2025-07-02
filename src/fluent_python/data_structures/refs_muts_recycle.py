import copy


def aliasing():
    """Example of aliasing in Python.

    >>> aliasing()
    True
    Id for lewis == id for charles: True
    Post change. lewis: {'name': 'Charles', 'age': 31}, charles: {'name': 'Charles', 'age': 31}
    """
    charles = {"name": "Charles", "age": 30}

    lewis = charles  # lewis is an alias for charles

    print(lewis is charles)  # True, both refer to the same object
    print(f"Id for lewis == id for charles: {id(lewis) == id(charles)}")

    lewis["age"] = 31  # This will change the age in both references
    print(
        f"Post change. lewis: {lewis}, charles: {charles}"
    )  # Both will show the updated age


def tuple_immutability():
    """Tuple immutability example.

    >>> tuple_immutability()
    Original tuple: (1, [2, 3])
    Modified tuple: (1, [2, 3, 4])
    Id before == id after: True
    """
    t = (1, [2, 3])
    print(f"Original tuple: {t}")

    original_id = id(t)

    t[-1].append(4)  # This modifies the list inside the tuple
    print(f"Modified tuple: {t}")

    print(f"Id before == id after: {id(t) == original_id}")


def shallow_copy():
    """Copies are shallow by default.

    >>> shallow_copy()
    l1: [1, [2, 3], 4], l2: [1, [2, 3], 4]
    Id for l1 != id for l2: True
    After appending 100 to l1, l1: [1, [2, 3], 4, 100], l2: [1, [2, 3], 4]
    After appending 5 to l2[1], l1: [1, [2, 3, 5], 4, 100], l2: [1, [2, 3, 5], 4]
    """
    l1 = [1, [2, 3], 4]
    l2 = l1[:]  # This creates a shallow copy of l1
    print(f"l1: {l1}, l2: {l2}")
    print(f"Id for l1 != id for l2: {id(l1) != id(l2)}")

    l1.append(100)  # This modifies l1 but not l2.
    print(f"After appending 100 to l1, l1: {l1}, l2: {l2}")

    l2[1].append(5)  # This modifies the inner list in l1 as well
    print(f"After appending 5 to l2[1], l1: {l1}, l2: {l2}")


def deep_copy():
    """Same example as above but with deep copy.

    >>> deep_copy()
    l1: [1, [2, 3], 4], l2: [1, [2, 3], 4]
    Id for l1 != id for l2: True
    After appending 100 to l1, l1: [1, [2, 3], 4, 100], l2: [1, [2, 3], 4]
    After appending 5 to l2[1], l1: [1, [2, 3], 4, 100], l2: [1, [2, 3, 5], 4]
    """
    l1 = [1, [2, 3], 4]
    l2 = copy.deepcopy(l1)  # This creates a shallow copy of l1
    print(f"l1: {l1}, l2: {l2}")
    print(f"Id for l1 != id for l2: {id(l1) != id(l2)}")

    l1.append(100)  # This modifies l1 but not l2.
    print(f"After appending 100 to l1, l1: {l1}, l2: {l2}")

    l2[1].append(5)  # This modifies the inner list in l1 as well
    print(f"After appending 5 to l2[1], l1: {l1}, l2: {l2}")


def func_params_as_refs(a, b):
    """Function to demonstrate that parameters are passed by reference in Python.

    Primitives are immutable, so they behave like pass by value.
    >>> x = 1
    >>> y = 2
    >>> func_params_as_refs(1, 2)
    3
    >>> x, y
    (1, 2)

    Others are mutable, so they behave like pass by reference.
    >>> a = [1, 2]
    >>> b = [3, 4]
    >>> func_params_as_refs(a, b)
    [1, 2, 3, 4]
    >>> a, b
    ([1, 2, 3, 4], [3, 4])
    """
    a += b
    return a


class Bus:
    def __init__(self, passengers=[]):
        self.passengers: list[str] = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


def muts_as_param_defaults():
    """Demonstrate issues with mutable default arguments.

    >>> muts_as_param_defaults()
    Bus1 passengers: ['Alice', 'Bob']
    Bus1 passengers after changes: ['Bob', 'Charlie']. As expected
    Bus2 passengers: ['Charlie']
    Bus3 passengers: ['Charlie']. This is not as expected, should be empty
    Bus3 passengers after picking Dave: ['Charlie', 'Dave'].
    Bus2 passengers after bus3 changes: ['Charlie', 'Dave']. Dave is here too!
    Bus2 passengers is bus3 passengers: True.
    bus1.passengers is bus2.passengers: False. Distinct as bus1 didn't use default.
    """
    bus1 = Bus(["Alice", "Bob"])
    print(f"Bus1 passengers: {bus1.passengers}")

    bus1.pick("Charlie")
    bus1.drop("Alice")
    print(f"Bus1 passengers after changes: {bus1.passengers}. As expected")

    bus2 = Bus()
    bus2.pick("Charlie")
    print(f"Bus2 passengers: {bus2.passengers}")

    # This is using the same default list as bus2
    bus3 = Bus()
    print(
        f"Bus3 passengers: {bus3.passengers}. This is not as expected, should be empty"
    )

    bus3.pick("Dave")
    print(f"Bus3 passengers after picking Dave: {bus3.passengers}.")
    print(f"Bus2 passengers after bus3 changes: {bus2.passengers}. Dave is here too!")

    print(f"Bus2 passengers is bus3 passengers: {bus2.passengers is bus3.passengers}.")

    print(
        f"bus1.passengers is bus2.passengers: {bus1.passengers is bus2.passengers}. Distinct as bus1 didn't use default.",
    )


class StillBadBus:
    def __init__(self, passengers: list[str] | None = None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


def mut_received_args():
    """Demonstrate that mutable arguments are not recycled.

    >>> mut_received_args()
    Original team: ['LeBron James', 'Anthony Davis', 'Russell Westbrook']
    After bus dropped Westbrook: ['LeBron James', 'Anthony Davis']. This is not as expected, should be unchanged.
    """
    basketball_team = ["LeBron James", "Anthony Davis", "Russell Westbrook"]
    print(f"Original team: {basketball_team}")

    bus = StillBadBus(basketball_team)
    bus.drop("Russell Westbrook")
    print(
        f"After bus dropped Westbrook: {basketball_team}. This is not as expected, should be unchanged."
    )


class BestBus:
    def __init__(self, passengers: list[str] | None = None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)  # Creates a copy

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


def mut_received_args_fixed():
    """Demonstrate that mutable arguments are recycled.

    >>> mut_received_args_fixed()
    Original team: ['LeBron James', 'Anthony Davis', 'Russell Westbrook']
    After bus dropped Westbrook: ['LeBron James', 'Anthony Davis', 'Russell Westbrook']. This is as expected, team is unchanged.
    Bus1 passengers: ['Alice', 'Bob']
    Bus1 passengers after changes: ['Bob', 'Charlie']. As expected
    Bus2 passengers: ['Charlie']
    Bus3 passengers: []. Empty as expected, no default list used
    Bus3 passengers after picking Dave: ['Dave'].
    Bus2 passengers after bus3 changes: ['Charlie']. Dave is not here
    Bus2 passengers is bus3 passengers: False.
    """
    basketball_team = ["LeBron James", "Anthony Davis", "Russell Westbrook"]
    print(f"Original team: {basketball_team}")

    bus = BestBus(basketball_team)
    bus.drop("Russell Westbrook")
    print(
        f"After bus dropped Westbrook: {basketball_team}. This is as expected, team is unchanged."
    )

    bus1 = BestBus(["Alice", "Bob"])
    print(f"Bus1 passengers: {bus1.passengers}")

    bus1.pick("Charlie")
    bus1.drop("Alice")
    print(f"Bus1 passengers after changes: {bus1.passengers}. As expected")

    bus2 = BestBus()
    bus2.pick("Charlie")
    print(f"Bus2 passengers: {bus2.passengers}")

    # This is using the same default list as bus2
    bus3 = BestBus()
    print(
        f"Bus3 passengers: {bus3.passengers}. Empty as expected, no default list used"
    )

    bus3.pick("Dave")
    print(f"Bus3 passengers after picking Dave: {bus3.passengers}.")
    print(f"Bus2 passengers after bus3 changes: {bus2.passengers}. Dave is not here")

    print(f"Bus2 passengers is bus3 passengers: {bus2.passengers is bus3.passengers}.")
