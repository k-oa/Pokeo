from icecream import ic

from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.utils.magic_filter import MagicFilter

from bot import bot
from models.player import Player
from models.pokemon import Pokemon, Nature, parse_learn_entry
from services.pokemon import PokemonRepository
from services import pokemon, pokedex
# from i18n import _

router = Router()


@router.message(Command('ping'))
async def ping(message: Message):
    await message.answer('pong')

    poke = await pokemon.PokemonFactory.create('pikachu', 5, 6)
    ic(poke)


@router.message(F.chat.id == F.from_user.id)
async def battle_chat(message: Message, player: Player):
    ...
    # player = await mongo.players.get({'_id': message.from_user.id})
    # if player['battle']:
    #     players = (await mongo.games.get({'_id': player['battle']}))['players']
    #     send_to_players = [player for player in players if type(player) == int and not player == message.from_user.id]
    #     for player in send_to_players:
    #         await bot.send_message(player, message.text)