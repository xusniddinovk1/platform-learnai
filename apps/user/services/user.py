from apps.user.dto.register import RegisterEmailRequestDTO
from apps.user.models import User
from apps.user.repositories.user import UserRepository


class UserService:
    """
    Service is for working with users
    """

    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository

    def create_user(self, dto: RegisterEmailRequestDTO) -> User:
        user = User(
            username=dto["username"],
            first_name=dto["first_name"],
            last_name=dto["last_name"],
            email=dto["email"],
        )
        user.set_password(dto["password"])
        return self.user_repository.create(user)

    def get_user_by_id(self, id: int) -> User | None:
        return self.user_repository.get_by_id(id)

    def get_user_by_email(self, email: str) -> User | None:
        return self.user_repository.get_by_email(email)

    def is_user_exists(self, email: str) -> bool:
        return self.user_repository.exists_email(email=email)

    def update_user(self, user: User) -> User:
        return self.user_repository.update(user)
