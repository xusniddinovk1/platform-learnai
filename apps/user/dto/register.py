from typing import TypedDict
from apps.user.dto.user import UserDTO


class RegisterEmailRequestDTO(TypedDict):
    username: str
    email: str
    password: str
    first_name: str
    last_name: str


class RegisterEmailResponseDTO(TypedDict):
    username: str
    email: str
    phone: str
    first_name: str
    last_name: str
    user: UserDTO
