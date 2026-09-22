from dataclasses import dataclass


@dataclass(frozen=True)
class UnknownTag:
    id: str
