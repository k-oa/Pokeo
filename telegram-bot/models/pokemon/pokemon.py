from dataclasses import dataclass
from .enums import Gender, Nature
from .stats import Stats


@dataclass
class PokedexEntry:
    name: str
    id: str
    num: int
    types: list[str]
    abilities: list[str]
    hidden_ability: str | None
    gender: Gender
    gender_ratio: float  # -1 genderless, 0.0-1.0 male ratio
    weight: float
    height: float
    stats: Stats

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
            
        stats = Stats.from_dict(data['baseStats'])

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
            stats=stats
        )


@dataclass  
class Pokemon:
    uid: int
    species: PokedexEntry
    name: str
    gender: Gender
    level: int
    experience: int
    iv: Stats
    ev: Stats
    nature: Nature
    ability: str
    moves: list[str]
    trainer: int | None
    shiny: bool

    @classmethod
    def from_dict(cls, data: dict, pokedex_entry: PokedexEntry) -> "Pokemon":
        return cls(
            uid=data['_id'],
            species=pokedex_entry,
            name=data['name'],
            gender=data['gender'],
            level=data['level'],
            experience=data['experience'],
            iv=Stats.from_dict(data['iv']),
            ev=Stats.from_dict(data['ev']),
            nature=Nature(data['nature']),
            ability=data['ability'],
            moves=data['moves'],
            trainer=data['trainer'],
            shiny=data['shiny']
        )
    
    def to_dict(self) -> dict:
        iv = self.iv.to_dict()
        ev = self.ev.to_dict()
        
        return {
            '_id': self.uid,
            'species': self.species.id,
            'name': self.name,
            'gender': self.gender,
            'level': self.level,
            'experience': self.experience,
            'iv': iv,
            'ev': ev,
            'nature': self.nature.value,
            'ability': self.ability,
            'moves': self.moves,
            'trainer': self.trainer,
            'shiny': self.shiny
        }