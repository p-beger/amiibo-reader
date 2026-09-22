from dataclasses import dataclass
from enum import StrEnum


class AmiiboSeries(StrEnum):
    ANIMAL_CROSSING = "Animal Crossing"
    DARK_SOULS = "Dark Souls"
    DETECTIVE_PIKACHU = "Detective Pikachu"
    DIABLO = "Diablo"
    FIRE_EMBLEM = "Fire Emblem"
    KIRBY = "Kirby"
    MEGA_MAN = "Mega Man"
    METROID = "Metroid"
    MONSTER_HUNTER = "Monster Hunter"
    PIKMIN = "Pikmin"
    POWER_UP_BANDS = "Power-Up Bands"
    SPLATOON = "Splatoon"
    SUPER_MARIO = "Super Mario"
    SUPER_MARIO_30TH = "Super Mario 30th"
    SUPER_SMASH_BROS = "Super Smash Bros."
    THE_LEGEND_OF_ZELDA = "The Legend of Zelda"
    THE_LEGEND_OF_ZELDA_30TH = "The Legend of Zelda 30th"
    THE_LEGEND_OF_ZELDA_BOTW = "The Legend of Zelda: Breath of the Wild"
    THE_LEGEND_OF_ZELDA_LA = "The Legend of Zelda: Link's Awakening"
    THE_LEGEND_OF_ZELDA_SS = "The Legend of Zelda: Skyward Sword"
    THE_LEGEND_OF_ZELDA_TOTK = "The Legend of Zelda: Tears of the Kingdom"
    THE_LEGEND_OF_ZELDA_TP = "The Legend of Zelda: Twilight Princess"
    XENOBLADE_CHRONICLES = "Xenoblade Chronicles"
    YOSHI_WOOLY_WORLD = "Yoshi's Wooly World"


@dataclass(frozen=True)
class Amiibo:
    id: str
    series: AmiiboSeries
    character: str
