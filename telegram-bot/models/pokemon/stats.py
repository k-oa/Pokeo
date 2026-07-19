from dataclasses import dataclass

@dataclass
class Stats:
    '''
    Simple container class to reference the fields by name instead of 
    index.
    '''
    hp : int
    attack : int
    defense : int
    special_attack : int
    special_defense : int
    speed : int

    @classmethod
    def from_dict(cls, data: dict) -> "Stats":
        return cls(data['hp'], data['atk'], data['def'], data['spa'], data['spd'], data['spe'])

    def to_dict(self):
        return {
            'hp': self.hp,
            'atk': self.attack,
            'def': self.defense,
            'spa': self.special_attack,
            'spd': self.special_defense,
            'spe': self.speed
        }