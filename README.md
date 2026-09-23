# amiibo-reader

Python library for reading amiibo tags with an MFRC522 RFID reader.

The library detects NFC tags, reads amiibo data from NTAG215 tags, and identifies amiibo figures using a local amiibo database.

`amiibo-reader` is an independant Python library for reading and parsing NFC data from amiibo tags. It is not affiliated with or endorsed by Nintendo.

## Features

- Read amiibo tags using an MFRC522 RFID reader
- Read NTAG215 data
- Extract amiibo IDs
- Identify amiibo figures from the local database
- Distinguish between recognized amiibo and unknown tags
- Expose a small and simple Python API

## How it works

When a tag is placed on the MFRC522 reader:

1. The reader detects the tag.
2. The tag UID is retrieved.
3. The library performs ISO14443A anticollision and selection.
4. The NTAG215 data is read.
5. The amiibo ID is extracted from the tag data.
6. The amiibo ID is looked up in the local amiibo database.
7. The corresponding `Amiibo` is returned if it is known.
8. Otherwise, an `UnknownTag` is returned.

If no tag is detected, `read_tag()` returns `None`.

## Requirements

- Python 3.13+
- Raspberry Pi or another compatible Linux system
- MFRC522 RFID reader
- amiibo figures or compatible NTAG215 tags
- SPI interface enabled

The library uses the `mfrc522` Python package to communicate with the MFRC522 reader.

## Installation

Clone the repository:

```bash
git clone https://github.com/p-beger/amiibo-reader.git
cd amiibo-reader
```

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

If creating the virtual environment fails, make sure `python3-full` is installed:

```bash
sudo apt-get install python3-full
```

Install the library:

```bash
python -m pip install .
```

For development, install the development dependencies:

```bash
python -m pip install --group dev
```

## MFRC522 configuration

The library currently uses the following MFRC522 configuration:
- SPI bus: 0
- SPI device: 0
- SPI speed: 1 MHz
- Reset pin: 22
SPI must be enabled on the Raspberry Pi.

The reader is automatically initialized when the library is imported.

## Usage

The main API is exposed directly from the `amiibo_reader` package:

```python
from amiibo_reader import close_reader, read_tag
```

Read a tag:

```python
tag = read_tag()

if tag is None:
    print("No tag detected")
else:
    print(tag)
```

## Recognized amiibo

When the tag is recognized, `read_tag()` returns an `Amiibo` object:

```python
from amiibo_reader import Amiibo, read_tag

tag = read_tag()

if isinstance(tag, Amiibo):
    print(f"ID: {tag.id}")
    print(f"Series: {tag.series}")
    print(f"Character: {tag.character}")
```

For example:
```
ID: 0000000000000002
Series: Super Smash Bros.
Character: Mario
```

## Unknown Tags

If a tag is detected but cannot be identified as a known amiibo, `read_tag()` returns an `UnknownTag` object:

```python
from amiibo_reader import UnknownTag, read_tag

tag = read_tag()

if isinstance(tag, UnknownTag):
    print(f"Unknown tag ID: {tag.id}")
```

The `id` contains the most relevant identifier available:
- the tag UID if the amiibo data could not be read
- the amiibo ID if the tag was successfully read but is not present in the local database

## No tag detected

If not tag is present:

```python
tag = read_tag()

if tag is None:
    print("No tag detected")
```

## Closing the reader

When the reader is no longer needed, close it with:

```python
from amiibo_reader import close_reader

close_reader()
```

## amiibo database

The amiibo database is stored in `amiibos.py`.

Each entry associates an amiibo ID with an `Amiibo` object.

```python
AMIIBOS: dict[str, Amiibo] = {
    "0000000000000002": Amiibo(
        "0000000000000002",
        AmiiboSeries.SUPER_SMASH_BROS,
        "Mario",
    ),
}
```

Additional amiibo can be added to the database by adding their amiibo ID, series and character.

## Project structure

```
amiibo-reader/
├── src/
│   └── amiibo_reader/
│       ├── __init__.py
│       ├── amiibo.py
│       ├── amiibos.py
│       ├── read_tag.py
│       └── unknown_tag.py
├── .gitignore
├── pyproject.toml
└── README.md
```

## Development

The project uses:
- Ruff for formatting and linting
- mypy for static type checking

Format the code with Ruff:

```bash
ruff format .
```

Lint the code:

```bash
ruff check .
```

Run mypy:

```bash
mypy src
```