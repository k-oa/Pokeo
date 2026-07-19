from models.pokemon import PokedexEntry, Pokemon, Stats, Nature, Gender
from services.pokedex import get_pokedex_entry, get_moveset
import random


class PokemonFactory:
    @staticmethod
    async def create(pokemon_id: str, min_level: int, max_level: int) -> dict:

        entry = await get_pokedex_entry(pokemon_id)
        moveset = await get_moveset(pokemon_id)
        level = random.randint(min_level, max_level)
        
        return {
            'id': pokemon_id,
            'level': level,
            'iv': PokemonFactory._random_ivs().to_dict(),
            'nature': Nature.random(),
            'moves': moveset.get_level_up_moves_at_level(level)[-4:],
            'gender': PokemonFactory._generate_pokemon_gender(entry.gender, entry.gender_ratio)
            # ...
        }

    @staticmethod
    def _random_ivs() -> Stats:
        return Stats(
            random.randint(0, 31), 
            random.randint(0, 31), 
            random.randint(0, 31), 
            random.randint(0, 31), 
            random.randint(0, 31), 
            random.randint(0, 31))
    
    @staticmethod
    def _generate_pokemon_gender(gender: Gender, gender_ratio: float) -> Gender:
        if gender == Gender.BOTH:
            return Gender.MALE if random.random() < gender_ratio else Gender.FEMALE
        return gender