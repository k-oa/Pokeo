from icecream import ic

from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from bot import bot
# import mongo
# from i18n import _

router = Router()


@router.message(F.text == '👾')
async def downloaw(message: Message):
    await message.answer('👾')


@router.message(Command('ping'))
async def ping(message: Message):
    await message.answer('pong')


@router.message()
async def battle_chat(message: Message):
    if message.chat.id == message.from_user.id:
        ...
        # player = await mongo.players.get({'_id': message.from_user.id})
        # if player['battle']:
        #     players = (await mongo.games.get({'_id': player['battle']}))['players']
        #     send_to_players = [player for player in players if type(player) == int and not player == message.from_user.id]
        #     for player in send_to_players:
        #         await bot.send_message(player, message.text)