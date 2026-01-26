"""
Exercise 3: Set Operations
TASK: Write tests for the provided function

The function find_common_and_unique is provided below.
- Write at least 5 tests that verify it works correctly.
- Consider: basic cases, empty sets, no overlap, complete overlap, subset relationships, etc
- Write descriptive test function names such as:
    - test_find_common_and_unique_basic()
    - test_find_common_and_unique_no_overlap()
    - test_find_common_and_unique_complete_overlap()
    - test_find_common_and_unique_empty_sets()
"""


def find_common_and_unique(set_a: set[str], set_b: set[str]) -> dict[str, set[str]]:
    """
    Find common elements and unique elements in two sets.

    Args:
        set_a: First set of strings
        set_b: Second set of strings

    Returns:
        Dictionary with keys:
        - 'common': elements in both sets (intersection)
        - 'only_a': elements only in set_a (difference)
        - 'only_b': elements only in set_b (difference)
    """
    return {
        'common': set_a & set_b,
        'only_a': set_a - set_b,
        'only_b': set_b - set_a
    }

def test_find_common_and_unique_basic():
    set_a = {"apple", "orange", "grape"}
    set_b = {"orange", "lemon", "peach"}
    result = find_common_and_unique(set_a, set_b)
    assert result == {
        'common': {"orange"},
        'only_a': {"apple", "grape"},
        'only_b': {"lemon", "peach"}
    }

def test_find_common_and_unique_no_overlap():
    set_a = {"apple", "orange"}
    set_b = {"grape", "lemon"}
    result = find_common_and_unique(set_a, set_b)
    assert result == {
        'common': set(),
        'only_a': {"apple", "orange"},
        'only_b': {"grape", "lemon"}
    }

def test_find_common_and_unique_complete_overlap():
    set_a = {"apple", "orange"}
    set_b = {"apple", "orange"}
    result = find_common_and_unique(set_a, set_b)
    assert result == {
        'common': {"apple", "orange"},
        'only_a': set(),
        'only_b': set()
    }

def test_find_common_and_unique_empty_sets():
    set_a = set()
    set_b = set()
    result = find_common_and_unique(set_a, set_b)
    assert result == {
        'common': set(),
        'only_a': set(),
        'only_b': set()
    }

test_find_common_and_unique_basic()
test_find_common_and_unique_no_overlap()
test_find_common_and_unique_complete_overlap()
test_find_common_and_unique_empty_sets()