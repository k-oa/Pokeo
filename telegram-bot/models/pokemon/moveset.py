from dataclasses import dataclass
from enum import Enum
import re
from icecream import ic


class LearnMethod(Enum):
    LEVEL_UP = "L"
    TM       = "M"
    EGG      = "E"
    TUTOR    = "T"
    EVENT    = "S"
    TRANSFER = "V"


@dataclass
class LearnableMove:
    move_id: str
    method: LearnMethod
    generation: int
    level: int | None      # only for level-up (L)
    event_index: int | None  # only for event (S)


def parse_learn_entry(move_id: str, code: str) -> LearnableMove:
    match  = re.fullmatch(r'(\d+)([LMETSVX])(\d*)', code)
    gen    = int(match.group(1))
    method = LearnMethod(match.group(2))
    extra  = int(match.group(3)) if match.group(3) else None

    return LearnableMove(
        move_id=move_id,
        method=method,
        generation=gen,
        level=extra if method == LearnMethod.LEVEL_UP else None,
        event_index=extra if method == LearnMethod.EVENT else None,
    )

@dataclass
class Moveset:
    moves: list[LearnableMove]

    def _resolve_generation(self, gen: int | None) -> int | None:
        if gen is not None:
            return gen
        return max((move.generation for move in self.moves), default=None)

    def get_level_up_moves_at_level(self, level: int, gen: int | None = None) -> list[LearnableMove]:
        target_gen = self._resolve_generation(gen)
        if target_gen is None:
            return []

        available_moves = [
            move for move in self.moves
            if move.method == LearnMethod.LEVEL_UP
            and move.generation == target_gen
            and move.level is not None
            and move.level <= level
        ]
        
        return sorted(available_moves, key=lambda m: m.level)
    
    def get_moves_at_level(self, level: int, gen: int | None = None) -> list[LearnableMove]:
        target_gen = self._resolve_generation(gen)
        if target_gen is None:
            return []

        available_moves = [
            move for move in self.moves
            if move.generation == target_gen
            and move.level is not None
            and move.level <= level
        ]
        
        return sorted(available_moves, key=lambda m: m.level)

    @classmethod
    def from_dict(cls, data: dict[str, list[str]]) -> "Moveset":
        moves: list[LearnableMove] = []
        for move_id, codes in data.items():
            for code in codes:
                moves.append(parse_learn_entry(move_id, code))
        return cls(moves=moves)
