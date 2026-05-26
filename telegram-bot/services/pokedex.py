import aiohttp
from icecream import ic

from models.pokemon import PokedexEntry

async def get_pokedex_entry(id: str) -> dict:
    async with aiohttp.ClientSession() as session:
        response = await session.get(f'http://localhost:3000/api/pokedex/{id}')
        # resp2 = await session.get(f'http://localhost:3000/api/learnset/{id}')
        # r = await resp2.json()
        # ic(r)
        data = await response.json()
        pokedex_entry = PokedexEntry.from_dict(data)
        return pokedex_entry