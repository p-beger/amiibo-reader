from .amiibo import Amiibo, AmiiboSeries

AMIIBOS: dict[str, Amiibo] = {
    # Animal Crossing
    # Not implemented yet
    #
    # Dark Souls
    # Not implemented yet
    #
    # Detective Pikachu
    # Not implemented yet
    #
    # Diablo
    # Not implemented yet
    #
    # Fire Emblem
    # Not implemented yet
    #
    # Kirby
    # Not implemented yet
    #
    # Mega Man
    # Not implemented yet
    #
    # Metroid
    # Not implemented yet
    #
    # Monster Hunter
    # Not implemented yet
    #
    # Pikmin
    # Not implemented yet
    #
    # Power-Up Bands
    # Not implemented yet
    #
    # Splatoon
    # Not implemented yet
    #
    # Super Mario
    # Not implemented yet
    #
    # Super Mario 30th
    # Not implemented yet
    #
    # Super Smash Bros.
    # Not completed yet
    "0000000000000002": Amiibo("0000000000000002", AmiiboSeries.SUPER_SMASH_BROS, "Mario"),
    "0002000000010002": Amiibo("0002000000010002", AmiiboSeries.SUPER_SMASH_BROS, "Peach"),
    "0003000000020002": Amiibo("0003000000020002", AmiiboSeries.SUPER_SMASH_BROS, "Yoshi"),
    "0008000000030002": Amiibo("0008000000030002", AmiiboSeries.SUPER_SMASH_BROS, "Donkey Kong"),
    "0100000000040002": Amiibo("0100000000040002", AmiiboSeries.SUPER_SMASH_BROS, "Link"),
    "0580000000050002": Amiibo("0580000000050002", AmiiboSeries.SUPER_SMASH_BROS, "Fox"),
    "05C0000000060002": Amiibo("05C0000000060002", AmiiboSeries.SUPER_SMASH_BROS, "Samus"),
    "0700000000070002": Amiibo("0700000000070002", AmiiboSeries.SUPER_SMASH_BROS, "Wii Fit Trainer"),
    "0180000000080002": Amiibo("0180000000080002", AmiiboSeries.SUPER_SMASH_BROS, "Villager"),
    "1919000000090002": Amiibo("1919000000090002", AmiiboSeries.SUPER_SMASH_BROS, "Pikachu"),
    "1F000000000A0002": Amiibo("1F000000000A0002", AmiiboSeries.SUPER_SMASH_BROS, "Kirby"),
    "21000000000B0002": Amiibo("21000000000B0002", AmiiboSeries.SUPER_SMASH_BROS, "Marth"),
    "01010000000E0002": Amiibo("01010000000E0002", AmiiboSeries.SUPER_SMASH_BROS, "Zelda"),
    "00090000000D0002": Amiibo("00090000000D0002", AmiiboSeries.SUPER_SMASH_BROS, "Diddy Kong"),
    "00010000000C0002": Amiibo("00010000000C0002", AmiiboSeries.SUPER_SMASH_BROS, "Luigi"),
    "06C00000000F0002": Amiibo("06C00000000F0002", AmiiboSeries.SUPER_SMASH_BROS, "Little Mac"),
    "0740000000100002": Amiibo("0740000000100002", AmiiboSeries.SUPER_SMASH_BROS, "Pit"),
    "0600000000120002": Amiibo("0600000000120002", AmiiboSeries.SUPER_SMASH_BROS, "Captain Falcon"),
    "0004010000130002": Amiibo("0004010000130002", AmiiboSeries.SUPER_SMASH_BROS, "Rosalina"),
    "0005000000140002": Amiibo("0005000000140002", AmiiboSeries.SUPER_SMASH_BROS, "Bowser"),
    "1AC0000000110002": Amiibo("1AC0000000110002", AmiiboSeries.SUPER_SMASH_BROS, "Lucario"),
    "0100010000160002": Amiibo("0100010000160002", AmiiboSeries.SUPER_SMASH_BROS, "Toon Link"),
    "0101010000170002": Amiibo("0101010000170002", AmiiboSeries.SUPER_SMASH_BROS, "Sheik"),
    "2101000000180002": Amiibo("2101000000180002", AmiiboSeries.SUPER_SMASH_BROS, "Ike"),
    "22400000002B0002": Amiibo("22400000002B0002", AmiiboSeries.SUPER_SMASH_BROS, "Shulk"),
    "3200000000300002": Amiibo("3200000000300002", AmiiboSeries.SUPER_SMASH_BROS, "Sonic"),
    "3480000000310002": Amiibo("3480000000310002", AmiiboSeries.SUPER_SMASH_BROS, "Mega Man"),
    "1F02000000280002": Amiibo("1F02000000280002", AmiiboSeries.SUPER_SMASH_BROS, "King Dedede"),
    "1F01000000270002": Amiibo("1F01000000270002", AmiiboSeries.SUPER_SMASH_BROS, "Meta Knight"),
    "21030000002A0002": Amiibo("21030000002A0002", AmiiboSeries.SUPER_SMASH_BROS, "Robin"),
    "2102000000290002": Amiibo("2102000000290002", AmiiboSeries.SUPER_SMASH_BROS, "Lucina"),
    "00070000001A0002": Amiibo("00070000001A0002", AmiiboSeries.SUPER_SMASH_BROS, "Wario"),
    "1906000000240002": Amiibo("1906000000240002", AmiiboSeries.SUPER_SMASH_BROS, "Charizard"),
    "22800000002C0002": Amiibo("22800000002C0002", AmiiboSeries.SUPER_SMASH_BROS, "Ness"),
    "3340000000320002": Amiibo("3340000000320002", AmiiboSeries.SUPER_SMASH_BROS, "Pac Man"),
    "1B92000000250002": Amiibo("1B92000000250002", AmiiboSeries.SUPER_SMASH_BROS, "Greninja"),
    "07420000001F0002": Amiibo("07420000001F0002", AmiiboSeries.SUPER_SMASH_BROS, "Palutena"),
    "0741000000200002": Amiibo("0741000000200002", AmiiboSeries.SUPER_SMASH_BROS, "Dark Pit"),
    "05C00100001D0002": Amiibo("05C00100001D0002", AmiiboSeries.SUPER_SMASH_BROS, "Zero Suit Samus"),
    "01020100001B0002": Amiibo("01020100001B0002", AmiiboSeries.SUPER_SMASH_BROS, "Ganondorf"),
    "0000010000190002": Amiibo("0000010000190002", AmiiboSeries.SUPER_SMASH_BROS, "Dr. Mario"),
    "0006000000150002": Amiibo("0006000000150002", AmiiboSeries.SUPER_SMASH_BROS, "Bowser Jr."),
    "06400100001E0002": Amiibo("06400100001E0002", AmiiboSeries.SUPER_SMASH_BROS, "Olimar"),
    #
    # The Legend of Zelda
    # Not implemented yet
    #
    # The Legend of Zelda 30th
    # Not implemented yet
    #
    # The Legend of Zelda: Breath of the Wild
    # Not implemented yet
    #
    # The Legend of Zelda: Link's Awakening
    # Not implemented yet
    #
    # The Legend of Zelda: Skyward Sword
    # Not implemented yet
    #
    # The Legend of Zelda: Tears of the Kingdom
    # Not implemented yet
    #
    # The Legend of Zelda: Twilight Princess
    # Not implemented yet
    #
    # Xenoblade Chronicles
    # Not implemented yet
    #
    # Yoshi's Wooly World
    # Not implemented yet
    #
}
