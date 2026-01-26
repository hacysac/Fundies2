"""
Exercise 5: Dictionaries
TASK: Write both the function and tests

Create a function called personality_mapping that:
- Takes a dictionary mapping villager names to personality types: {"Maple": "Normal", "Raymond": "Smug", "Sherb": "Lazy"}
- Returns a dictionary mapping personality types to lists of villager names: {"Normal": ["Maple"], "Smug": ["Raymond"], "Lazy": ["Sherb"]}
"""


def personality_mapping(villagers: dict[str, str]) -> dict[str, list[str]]:
    """
    Invert a villager-to-personality mapping to a personality-to-villagers mapping.

    Args:
        villagers: Dictionary mapping villager name to personality type

    Returns:
        Dictionary mapping personality type to sorted list of villager names
    """
    result = {}
    for name, personality in villagers.items():
        if personality in result:
            result[personality].append(name)
        else:
            result[personality] = [name]
    return result


def test_personality_mapping_basic():
    villagers = {
        "Maple": "Normal",
        "Raymond": "Smug",
        "Sherb": "Lazy"
    }
    assert personality_mapping(villagers) == {
        "Normal": ["Maple"],
        "Smug": ["Raymond"],
        "Lazy": ["Sherb"]
    }

def test_personality_mapping_multiple():
    villagers = {
        "Maple": "Normal",
        "Stitches": "Normal",
        "Raymond": "Smug",
        "Bob": "Smug"
    }
    assert personality_mapping(villagers) == {
        "Normal": ["Maple", "Stitches"],
        "Smug": ["Raymond", "Bob"]
    }

def test_personality_mapping_empty():
    villagers = {}
    assert personality_mapping(villagers) == {}

test_personality_mapping_basic()
test_personality_mapping_multiple()
test_personality_mapping_empty()