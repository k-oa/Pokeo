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