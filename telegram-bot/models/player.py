from dataclasses import dataclass, field
from models.enums import PlayerStatus


@dataclass
class Player:
    telegram_id: int
    status: PlayerStatus = PlayerStatus.UNREGISTERED

    in_game: bool = False
    game_id: int = 0

    team: list[int] = field(default_factory=list)

    @classmethod
    def from_dict(cls, data: dict) -> "Player":
        return cls(
            telegram_id=data["_id"],
            status=PlayerStatus(data.get("status")),

            # in_game=data.get("in_game", False),
            # game_id=data.get("game_id", 0),

            team=data.get("team", []),
        )