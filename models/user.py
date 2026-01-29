from dataclasses import dataclass
from typing import List
from enum import Enum


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: Enum
    phone: str
    birth_date: str
    subjects: str
    hobbies: List[Enum]
    picture: str
    address: str
    state: str
    city: str