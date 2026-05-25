from dataclasses import dataclass
from models.enums import Gender

@dataclass
class PokedexEntry:
    name: str
    id: str
    num: int
    types: list[str]
    abilities: list[str]
    hidden_ability: str | None
    gender: Gender
    gender_ratio: float  # -1 unknown, 0.0-1.0 male ratio
    weight: float
    height: float

    hp: int
    attack: int
    defense: int
    special_attack: int
    special_defense: int
    speed: int

    @classmethod
    def from_dict(cls, data: dict) -> "PokedexEntry":
        abilities = [data['abilities']['0']]
        if '1' in data['abilities']:
            abilities.append(data['abilities']['1'])

        gender_ratio = data.get('genderRatio').get('M')

        match data.get('gender'):
            case 'N':
                gender = Gender.GENDERLESS
            case 'M':
                gender = Gender.MALE
            case 'F':
                gender = Gender.FEMALE
            case _:
                gender = Gender.BOTH

        return cls(
            name=data['baseSpecies'],
            id=data['id'],
            num=data['num'],
            types=data['types'],
            abilities=abilities,
            hidden_ability=data['abilities'].get('H'),
            gender=gender,
            gender_ratio=gender_ratio,
            weight=data['weightkg'],
            height=data['heightm'],
            hp=data['baseStats']['hp'],
            attack=data['baseStats']['atk'],
            defense=data['baseStats']['def'],
            special_attack=data['baseStats']['spa'],
            special_defense=data['baseStats']['spd'],
            speed=data['baseStats']['spe'],
        )

@dataclass  
class Pokemon:
    ...