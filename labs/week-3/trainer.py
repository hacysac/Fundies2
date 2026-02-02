#!/usr/bin/env python3

"""Trainer class for managing a team of Pokemon."""

from pokemon import *


class Trainer:
    """A Pokemon trainer who manages a team of Pokemon."""

    def __init__(self, name: str) -> None:
        """Initialise a new Trainer."""
        self.team = []
        self.team_size = 0
        self.name = name
        self.max_team_size = 6

    def add_to_team(self, pokemon: Pokemon) -> bool:
        """Add a Pokemon to the trainer's team.

        Returns True if successful, False if team is full.
        """
        if len(self.team) < self.max_team_size:
            self.team.append(pokemon)
            return True
        return False

    def get_team_size(self) -> int:
        """Get the number of Pokemon in the team."""
        return len(self.team)

    def get_first_available(self) -> Pokemon | None:
        """Get the first non-fainted Pokemon in the team."""
        for pokemon in self.team:
            if not pokemon.is_fainted():
                return pokemon
        return None

    def get_pokemon_by_type(self, pokemon_type: type) -> list[Pokemon]:
        """Get a list of all Pokemon in the team that are instances of pokemon_type."""
        result = []
        for pokemon in self.team:
            if pokemon.__class__ == pokemon_type:
                result.append(pokemon)
        return result

    def __str__(self) -> str:
        """Return a string representation of this Trainer."""
        return f"{self.name} ({len(self.team)}/{self.max_team_size})"


ash = Trainer("Ash")
ash.add_to_team(Pokemon("Pikachu", 35, 10, 5, "Shock", 40))
ash.add_to_team(FireType("Charmander", 39, 12, 8, "Ember", 40, 0.2))
ash.add_to_team(WaterType("Squirtle", 44, 9, 10, "Water Gun", 40, 5))

lily = Trainer("Lily")
lily.add_to_team(Pokemon("Pikachu", 35, 10, 5, "Shock", 40))

rocky = Trainer("Rocky")
rocky.add_to_team(Pokemon("Pikachu", 35, 10, 5, "Shock", 40))
rocky.add_to_team(FireType("Charmander", 39, 12, 8, "Ember", 40, 0.2))
rocky.add_to_team(FireType("Vulpix", 39, 12, 8, "Burn", 40, 0.2))
rocky.add_to_team(WaterType("Squirtle", 44, 9, 10, "Water Gun", 40, 5))
rocky.add_to_team(WaterType("Squirt", 44, 9, 10, "Splash", 40, 5))


assert ash.get_pokemon_by_type(FireType)[0].name == "Charmander"
assert ash.get_pokemon_by_type(WaterType)[0].name == "Squirtle"
assert lily.get_pokemon_by_type(FireType) == []
assert len(rocky.get_pokemon_by_type(FireType)) == 2
