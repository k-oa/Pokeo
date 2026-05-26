from icecream import ic

from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.utils.magic_filter import MagicFilter

from bot import bot
from models.player import Player
from models.pokemon import Pokemon, Nature
from services.pokemon import PokemonRepository
from services import pokemon, pokedex
# from i18n import _

router = Router()


@router.message(Command('ping'))
async def ping(message: Message):
    await message.answer('pong')
    
    iv = {
            'hp': 1,
            'atk': 2,
            'def': 3,
            'spa': 4,
            'spd': 5,
            'spe': 6
        }
    ev = {
            'hp': 6,
            'atk': 5,
            'def': 4,
            'spa': 3,
            'spd': 2,
            'spe': 1
        }
        
    poke_dict = {
            '_id': 1000,
            'species': 'squirtle',
            'name': 'Big Squirtle',
            'gender': 'F',
            'level': 10,
            'experience': 100,
            'iv': iv,
            'ev': ev,
            'nature': Nature.NAUGHTY,
            'ability': 'overgrow',
            'moves': ['watergun', 'tackle'],
            'trainer': 100_000,
            'shiny': False
        }
    entry = await pokedex.get_pokedex_entry('squirtle')
    created_poke = Pokemon.from_dict(poke_dict, entry)
    ic('a')
    p = PokemonRepository()
    await p.create(created_poke)
    ic('b')
    d = await p.get(created_poke.uid)
    ic(d)



@router.message(F.chat.id == F.from_user.id)
async def battle_chat(message: Message, player: Player):
    ...
    # player = await mongo.players.get({'_id': message.from_user.id})
    # if player['battle']:
    #     players = (await mongo.games.get({'_id': player['battle']}))['players']
    #     send_to_players = [player for player in players if type(player) == int and not player == message.from_user.id]
    #     for player in send_to_players:
    #         await bot.send_message(player, message.text)