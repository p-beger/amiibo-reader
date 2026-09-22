from __future__ import annotations

from typing import TYPE_CHECKING

from .amiibo import Amiibo
from .amiibos import AMIIBOS
from .unknown_tag import UnknownTag

if TYPE_CHECKING:
    from mfrc522 import MFRC522  # type: ignore[import-untyped]

reader: MFRC522 | None = None


def _get_reader() -> MFRC522:
    global reader

    if reader is None:
        from mfrc522 import MFRC522  # type: ignore[import-untyped]

        reader = MFRC522(bus=0, device=0, spd=1000000, pin_mode=10, pin_rst=22)

    return reader


def close_reader() -> None:
    global reader

    if reader is not None:
        reader.Close()
        reader = None


def _read_ntag_page(page: int) -> list[int] | None:
    reader = _get_reader()

    command = [0x30, page]

    crc = reader.CalulateCRC(command)
    command += crc[:2]

    reader.WriteReg(reader.BitFramingReg, 0x00)

    status, data, _ = reader.MFRC522_ToCard(reader.PCD_TRANSCEIVE, command)

    if status != reader.MI_OK:
        return None

    return data


def _anticoll_level(level: int) -> list[int] | None:
    """
    Performs ISO14443A anticollision.
    This function is used to retrieve the UID of a tag at a specific level (1 or 2).

    level 1 = 0x93
    level 2 = 0x95
    """

    reader = _get_reader()

    command = [level, 0x20]

    reader.WriteReg(reader.BitFramingReg, 0x00)

    status, data, _ = reader.MFRC522_ToCard(reader.PCD_TRANSCEIVE, command)

    if status != reader.MI_OK:
        return None

    if len(data) != 5:
        return None

    # BCC (Block Check Character) is the XOR of the first 4 bytes of the UID.
    bcc = data[0] ^ data[1] ^ data[2] ^ data[3]

    if bcc != data[4]:
        print("Invalid BCC")
        return None

    return data


def _select_level(level: int, uid_part: list[int]) -> bool:
    """
    Selects an ISO14443A UID level.

    uid_part = 5 bytes:
    - level 1: 88 + 3 bytes UID + BCC
    - level 2: 4 bytes UID + BCC
    """

    reader = _get_reader()

    command = [
        level,
        0x70,  # SELECT
        *uid_part,
    ]

    crc = reader.CalulateCRC(command)
    command += crc[:2]

    reader.WriteReg(reader.BitFramingReg, 0x00)

    status, _, _ = reader.MFRC522_ToCard(reader.PCD_TRANSCEIVE, command)

    return status == reader.MI_OK


def _select_amiibo() -> bool:
    """
    Select an amiibo by performing anticollision and SELECT operations
    for both UID levels.

    Amiibo UIDs use two ISO14443A cascade levels, so both levels must
    be processed before reading the NTAG215 data.
    """

    level1 = _anticoll_level(0x93)

    if not level1:
        print("Anticollision failed at level 1")
        return False

    if not _select_level(0x93, level1):
        print("Select failed at level 1")
        return False

    level2 = _anticoll_level(0x95)

    if not level2:
        print("Anticollision failed at level 2")
        return False

    if not _select_level(0x95, level2):
        print("Select failed at level 2")
        return False

    return True


def _get_amiibo_id(data: list[int]) -> str:
    """Extract the amiibo ID (first 8 bytes) from the tag data."""

    return bytes(data[:8]).hex().upper()


def read_tag() -> Amiibo | UnknownTag | None:
    """
    Read a tag and return the corresponding Amiibo object if recognized,
    otherwise return an UnknownTag object. Returns None if no tag is detected.
    """

    reader = _get_reader()

    status, _ = reader.Request(reader.PICC_REQIDL)

    if status != reader.MI_OK:
        return None

    _, uid = reader.Anticoll()
    uid = bytes(uid).hex().upper()

    if not _select_amiibo():
        return UnknownTag(uid)

    data = _read_ntag_page(21)

    if not data:
        return UnknownTag(uid)

    amiibo_id = _get_amiibo_id(data)

    return AMIIBOS.get(amiibo_id, UnknownTag(amiibo_id))
