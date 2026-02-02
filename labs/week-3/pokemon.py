#!/usr/bin/env python3

"""Pokemon classes for the battle system."""

import random


class Pokemon:
    """Base class for all Pokemon."""

    def __init__(
        self,
        name: str,
        max_hp: int,
        attack: int,
        defence: int,
        move: str,
        move_power: int,
    ) -> None:
        """Initialise a new Pokemon."""
        self.name = name
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.attack = attack
        self.defence = defence
        self.move = move
        self.move_power = move_power

    def take_damage(self, amount: int) -> None:
        """Reduce current_hp by amount (minimum 0)."""
        self.current_hp = max(0, self.current_hp - amount)

    def calculate_damage(self, defender: "Pokemon") -> int:
        """Calculate damage dealt to defender.

        Damage is a random value between 85% and 100% of max damage.
        Minimum damage is 1.
        """
        max_damage = int((self.attack / defender.defence) * self.move_power)
        min_damage = int(max_damage * 0.85)
        return max(1, random.randint(min_damage, max_damage))

    def is_fainted(self) -> bool:
        """Check if the Pokemon has fainted."""
        return self.current_hp <= 0

    def attack_move(self) -> str:
        """Return the attack message for this Pokemon."""
        return f"{self.name} uses {self.move}!"

    def description(self) -> str:
        """Return a description of this Pokemon."""
        return f"{self.name} is a normal type"

    def __str__(self) -> str:
        """Return a string representation of this Pokemon."""
        return f"{self.name}: {self.current_hp}/{self.max_hp} HP"


class FireType(Pokemon):
    """A Fire type Pokemon."""

    burn_chance = 0.0

    def __init__(
        self,
        name: str,
        max_hp: int,
        attack: int,
        defence: int,
        move: str,
        move_power: int,
        burn_chance: float,
    ) -> None:
        """Initialise a new Fire type Pokemon."""
        super().__init__(name, max_hp, attack, defence, move, move_power)
        self.burn_chance = burn_chance

    def description(self) -> str:
        """Return a description of this Fire type Pokemon."""
        return f"{self.name} is a fire type with a burn chance of {self.burn_chance * 100}%"


class WaterType(Pokemon):
    """A Water type Pokemon."""

    swim_speed = 0

    def __init__(
        self,
        name: str,
        max_hp: int,
        attack: int,
        defence: int,
        move: str,
        move_power: int,
        swim_speed: int,
    ) -> None:
        """Initialise a new Water type Pokemon."""
        super().__init__(name, max_hp, attack, defence, move, move_power)
        self.swim_speed = swim_speed

    def description(self) -> str:
        """Return a description of this Water type Pokemon."""
        return f"{self.name} is a water type with a swim speed of {self.swim_speed}"


# Normal types - Pokemon(name, max_hp, attack, defence, move, move_power)
pikachu = Pokemon("Pikachu", 35, 11, 7, "Quick Attack", 10)
eevee = Pokemon("Eevee", 55, 10, 8, "Tackle", 10)
snorlax = Pokemon("Snorlax", 160, 11, 10, "Body Slam", 20)
meowth = Pokemon("Meowth", 40, 9, 7, "Scratch", 10)

# Fire types - FireType(name, max_hp, attack, defence, move, move_power, burn_chance)
charmander = FireType("Charmander", 39, 12, 8, "Ember", 10, 0.2)
vulpix = FireType("Vulpix", 38, 9, 8, "Flamethrower", 22, 0.1)
ponyta = FireType("Ponyta", 50, 17, 11, "Flame Charge", 12, 0.1)

# Water types - WaterType(name, max_hp, attack, defence, move, move_power, swim_speed)
squirtle = WaterType("Squirtle", 44, 9, 10, "Water Gun", 10, 5)
psyduck = WaterType("Psyduck", 50, 10, 9, "Water Pulse", 15, 4)
staryu = WaterType("Staryu", 30, 9, 11, "Swift", 15, 7)

assert pikachu.__str__() == "Pikachu: 35/35 HP"
assert pikachu.is_fainted() == False
assert pikachu.attack_move() == "Pikachu uses Quick Attack!"

assert pikachu.description() == "Pikachu is a normal type"
assert (
    charmander.description() == "Charmander is a fire type with a burn chance of 20.0%"
)
assert squirtle.description() == "Squirtle is a water type with a swim speed of 5"
