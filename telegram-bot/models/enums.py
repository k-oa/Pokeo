from enum import Enum


class PlayerStatus(Enum):
    UNREGISTERED = "unregistered"  # the user is not in db yet
    ACTIVE = "active"
    BANNED = "banned"
    ADMIN = "admin"


class Gender(Enum):
    BOTH = "both"
    MALE = "male"
    FEMALE = "female"
    GENDERLESS = "genderless"