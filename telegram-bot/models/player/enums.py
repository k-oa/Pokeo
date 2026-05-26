from enum import Enum


class PlayerStatus(Enum):
    UNREGISTERED = "unregistered"  # the user is not in db yet
    ACTIVE = "active"
    BANNED = "banned"
    ADMIN = "admin"
