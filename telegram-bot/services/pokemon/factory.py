from models.pokemon import PokedexEntry, Pokemon, Stats, Nature
import random


class PokemonFactory:
    @staticmethod
    def generate(pokemon_id: str, min_level: int, max_level: int) -> dict:
        entry = PokedexEntry(pokemon_id)
        level = random.randint(min_level, max_level)
        
        return {
            'id': pokemon_id,
            'level': level,
            'iv': PokemonFactory._random_ivs(),
            'nature': PokemonFactory._random_nature(),
            'moves': entry.get_moves_for_level(level),
            # ...
        }

    @staticmethod
    def _random_ivs() -> list[int]:
        return [random.randint(0, 31) for _ in range(6)]

    @staticmethod
    def _random_nature() -> str:
        return Nature.random()