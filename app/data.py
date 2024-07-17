import uuid
from dataclasses import dataclass
from enum import Enum
from typing import Optional, Any


# DataDomain definitions
class DataDomain(Enum):
    Unknown = 'unknown'
    BeeldBank = 'beeldbank'
    Medicatie = 'medicatie'

    @classmethod
    def from_str(cls, label: str) -> Optional['DataDomain']:
        try:
            return cls(label.lower())
        except ValueError:
            return None

    def to_fhir(self) -> str:
        if self == DataDomain.BeeldBank:
            return 'ImagingStudy'
        if self == DataDomain.Medicatie:
            return 'MedicationRequest'
        return ""

    def __str__(self) -> str:
        return self.value


@dataclass
class UraNumber:
    def __init__(self, value: Any) -> None:
        if (isinstance(value, int) or isinstance(value, str)) and len(str(value)) <= 8 and str(value).isdigit():
            self.value = str(value).zfill(8)
        else:
            raise ValueError("URA number must be 8 digits or less")

    def __str__(self) -> str:
        return self.value

    def __repr__(self) -> str:
        return f"UraNumber({self.value})"


@dataclass
class Pseudonym:
    def __init__(self, value: Any) -> None:
        self.value = uuid.UUID(str(value))

    def __str__(self) -> str:
        return str(self.value)

    def __repr__(self) -> str:
        return f"Pseudonym({self.value})"
