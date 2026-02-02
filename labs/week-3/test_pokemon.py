import pytest
from pokemon import Pokemon, FireType, WaterType


@pytest.fixture
def pokemon():
    return Pokemon("Eevee", 55, 10, 8, "Tackle", 40)


@pytest.fixture
def fire_pokemon():
    return FireType("Charmander", 39, 12, 8, "Ember", 40, 0.2)


@pytest.fixture
def water_pokemon():
    return WaterType("Squirtle", 44, 9, 10, "Water Gun", 40, 5)


def test_current_hp(pokemon):
    assert pokemon.current_hp == pokemon.max_hp


def test_is_fainted(pokemon):
    assert not pokemon.is_fainted()
    pokemon.current_hp = 0
    assert pokemon.is_fainted()


def test_attack_move(pokemon):
    assert pokemon.attack_move() == "Eevee uses Tackle!"


def test_string_representation(pokemon):
    assert str(pokemon) == "Eevee: 55/55 HP"


def test_fire_type_description(fire_pokemon):
    assert (
        fire_pokemon.description()
        == "Charmander is a fire type with a burn chance of 20.0%"
    )


def test_water_type_description(water_pokemon):
    assert (
        water_pokemon.description() == "Squirtle is a water type with a swim speed of 5"
    )


def test_normal_type_description(pokemon):
    assert pokemon.description() == "Eevee is a normal type"
