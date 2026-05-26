from dataclasses import dataclass
from models.pokemon import Pokemon
from services.pokedex import get_pokedex_entry
from services import db


class PokemonRepository:
    def __init__(self):
        self.db = db.pokemon

    async def get(self, pokemon_uid) -> Pokemon | None:
        pokemon_dict = await self.db.get({'_id': pokemon_uid})
        entry = await get_pokedex_entry(pokemon_dict['species'])
        pokemon = Pokemon.from_dict(pokemon_dict, entry)
        return pokemon

    async def edit(self, pokemon: Pokemon) -> None:
        pokemon_dict = pokemon.to_dict()
        await self.db.edit({'_id': pokemon.uid}, pokemon_dict)

    async def create(self, pokemon: Pokemon) -> None:
        pokemon_dict = pokemon.to_dict()
        await self.db.create(pokemon_dict)