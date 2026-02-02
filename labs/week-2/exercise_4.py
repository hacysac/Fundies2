"""
Exercise 4: Dictionary Manipulation
TASK: Write the function to make the tests pass

Create a function called count_species that:
- Takes a list of villager tuples: (name: str, species: str)
- Returns a dictionary mapping each species to the count of villagers with that species
- Example: [("Maple", "Cub"), ("Raymond", "Cat"), ("Sherb", "Goat")] -> {"Cub": 1, "Cat": 1, "Goat": 1}
"""


def count_species(villagers: list[tuple[str, str]]) -> dict[str, int]:
    """
    Count how many villagers belong to each species.

    Args:
        villagers: List of tuples containing (name, species)

    Returns:
        Dictionary mapping species to count of villagers
    """
    result = {}
    for v in villagers:
        result[v[1]] = result.get(v[1], 0) + 1
    return result


def test_count_species_basic():
    villagers = [
        ("Maple", "Cub"),
        ("Raymond", "Cat"),
        ("Sherb", "Goat"),
        ("Marina", "Octopus"),
    ]
    assert count_species(villagers) == {"Cub": 1, "Cat": 1, "Goat": 1, "Octopus": 1}


def test_count_species_duplicates():
    villagers = [
        ("Maple", "Cub"),
        ("Stitches", "Cub"),
        ("Raymond", "Cat"),
        ("Bob", "Cat"),
    ]
    assert count_species(villagers) == {"Cub": 2, "Cat": 2}


def test_count_species_all_same():
    villagers = [("Ankha", "Cat"), ("Raymond", "Cat"), ("Bob", "Cat")]
    assert count_species(villagers) == {"Cat": 3}


def test_count_species_empty():
    assert count_species([]) == {}


def test_count_species_single():
    villagers = [("Audie", "Wolf")]
    assert count_species(villagers) == {"Wolf": 1}


def test_count_species_many_species():
    villagers = [
        ("Marshal", "Squirrel"),
        ("Judy", "Cub"),
        ("Apollo", "Eagle"),
        ("Fauna", "Deer"),
        ("Poppy", "Squirrel"),
    ]
    assert count_species(villagers) == {"Squirrel": 2, "Cub": 1, "Eagle": 1, "Deer": 1}


test_count_species_basic()
test_count_species_duplicates()
test_count_species_all_same()
test_count_species_empty()
test_count_species_single()
test_count_species_many_species()
