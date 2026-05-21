from enum import Enum


class PlayerStatus(Enum):
    UNKNOWN = "unknown"  # the user is not in db yet
    ACTIVE = "active"
    BANNED = "banned"
    ADMIN = "admin"