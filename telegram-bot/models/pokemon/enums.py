import random
from enum import Enum
from typing import Dict, Literal
from dataclasses import dataclass


class Gender(Enum):
    BOTH = "both"
    MALE = "M"
    FEMALE = "F"
    GENDERLESS = "N"


@dataclass(frozen=True)
class NatureStatModifiers:
    hp: float = 1.0
    attack: float = 1.0
    defense: float = 1.0
    special_attack: float = 1.0
    special_defense: float = 1.0
    speed: float = 1.0


class Nature(Enum):
    modifiers: NatureStatModifiers

    def __new__(cls, value: str, modifiers: NatureStatModifiers):
        obj = object.__new__(cls)
        obj._value_ = value
        obj.modifiers = modifiers
        return obj

    ADAMANT = ("adamant", NatureStatModifiers(attack=1.1, special_attack=0.9))
    BOLD    = ("bold", NatureStatModifiers(defense=1.1, attack=0.9))
    BRAVE   = ("brave", NatureStatModifiers(attack=1.1, speed=0.9))
    CALM    = ("calm", NatureStatModifiers(special_defense=1.1, attack=0.9))
    GENTLE  = ("gentle", NatureStatModifiers(special_defense=1.1, defense=0.9))
    HASTY   = ("hasty", NatureStatModifiers(speed=1.1, defense=0.9))
    IMPISH  = ("impish", NatureStatModifiers(defense=1.1, special_attack=0.9))
    JOLLY   = ("jolly", NatureStatModifiers(speed=1.1, special_attack=0.9))
    LAX     = ("lax", NatureStatModifiers(defense=1.1, special_defense=0.9))
    LONELY  = ("lonely", NatureStatModifiers(attack=1.1, defense=0.9))
    MILD    = ("mild", NatureStatModifiers(special_attack=1.1, defense=0.9))
    MODEST  = ("modest", NatureStatModifiers(special_attack=1.1, attack=0.9))
    NAIVE   = ("naive", NatureStatModifiers(speed=1.1, special_defense=0.9))
    NAUGHTY = ("naughty", NatureStatModifiers(attack=1.1, special_defense=0.9))
    QUIET   = ("quiet", NatureStatModifiers(special_attack=1.1, speed=0.9))
    RASH    = ("rash", NatureStatModifiers(special_attack=1.1, special_defense=0.9))
    RELAXED = ("relaxed", NatureStatModifiers(defense=1.1, speed=0.9))
    SASSY   = ("sassy", NatureStatModifiers(special_defense=1.1, speed=0.9))
    TIMID   = ("timid", NatureStatModifiers(speed=1.1, attack=0.9))

    BASHFUL = ("bashful", NatureStatModifiers())
    DOCILE  = ("docile", NatureStatModifiers())
    HARDY   = ("hardy", NatureStatModifiers())
    QUIRKY  = ("quirky", NatureStatModifiers())
    SERIOUS = ("serious", NatureStatModifiers())

    def __str__(self) -> str:
        return self._value_
    
    @classmethod
    def random(cls) -> "Nature":
        return random.choice(list(cls))
