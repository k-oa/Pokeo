from dataclasses import dataclass
from models.enums import PlayerStatus


@dataclass
class Player:
    telegram_id: int
    status: PlayerStatus = PlayerStatus.UNKNOWN

    in_game: bool = False
    game_id: int = 0

    team: list[int] = None

    @classmethod
    def from_dict(cls, data: dict) -> "Player":
        return cls(
            telegram_id=data["_id"],
            status=PlayerStatus(data.get("status", "unknown")),

            # in_game=data.get("in_game", False),
            # game_id=data.get("game_id", 0),
            # wins=data.get("wins", 0),
            # losses=data.get("losses", 0),

            team=data.get("team", []),
        )