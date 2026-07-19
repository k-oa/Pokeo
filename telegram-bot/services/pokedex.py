import aiohttp
from icecream import ic

from models.pokemon import PokedexEntry
from models.pokemon.moveset import Moveset

async def get_pokedex_entry(id: str) -> PokedexEntry:
    async with aiohttp.ClientSession() as session:
        response = await session.get(f'http://localhost:3000/api/pokedex/{id}')
        data = await response.json()
        pokedex_entry = PokedexEntry.from_dict(data)
        return pokedex_entry


async def get_moveset(id: str) -> Moveset:
    async with aiohttp.ClientSession() as session:
        response = await session.get(f'http://localhost:3000/api/learnset/{id}')
        data = await response.json()
        moveset = Moveset.from_dict(data)
        return moveset