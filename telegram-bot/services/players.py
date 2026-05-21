from models.player import Player
from services import db


async def get_player(telegram_id: int) -> Player | None:
    data = await db.players.get({'_id': telegram_id})
    if not data:
        return Player(telegram_id)
    return Player.from_dict(data)