from typing import TypedDict


class UserDTO(TypedDict):
    id: int
    email: str
    phone: str | None
    username: str
    first_name: str
    last_name: str
