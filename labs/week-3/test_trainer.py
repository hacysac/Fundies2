import pytest
from trainer import Trainer
from pokemon import Pokemon, FireType, WaterType


@pytest.fixture
def pokemon():
    return Pokemon("Eevee", 55, 10, 8, "Tackle", 40)


@pytest.fixture
def trainer():
    trainer = Trainer("Ash")
    trainer.add_to_team(Pokemon("Pikachu", 35, 10, 5, "Shock", 40))
    trainer.add_to_team(FireType("Charmander", 39, 12, 8, "Ember", 40, 0.2))
    trainer.add_to_team(WaterType("Squirtle", 44, 9, 10, "Water Gun", 40, 5))
    return trainer


def test_add_to_team(trainer):
    assert trainer.get_team_size() == 3
    trainer.add_to_team(pokemon)
    assert trainer.get_team_size() == 4


def test_max_team_size(trainer):
    for i in range(6):
        trainer.add_to_team(pokemon)
    assert trainer.get_team_size() == 6
    assert not trainer.add_to_team(pokemon)
    assert trainer.get_team_size() == 6


def test_get_first_available(trainer):
    first_pokemon = trainer.get_first_available()
    assert first_pokemon.name == "Pikachu"


def test_fainted_pokemon(trainer):
    first_pokemon = trainer.get_first_available()
    first_pokemon.current_hp = 0  # Faint Pikachu
    second_pokemon = trainer.get_first_available()
    assert second_pokemon.name == "Charmander"


def test_all_fainted(trainer):
    for pokemon in trainer.team:
        pokemon.current_hp = 0  # Faint all Pokemon
    assert trainer.get_first_available() is None


def test_str_rep(trainer):
    assert str(trainer) == "Ash (3/6)"
