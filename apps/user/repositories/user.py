from django.db.models import QuerySet
from apps.user.models import User


class UserRepository:
    """
    Repository is for working with user
    """

    def create(self, user: User) -> User:
        user.save()
        return user

    def list(self) -> QuerySet[User]:
        return User.objects.all()

    def update(self, user: User) -> User:
        user.save()
        return user

    def delete(self, user: User) -> None:
        user.delete()

    def exists_email(self, email: str) -> bool:
        return User.objects.filter(email=email).exists()

    def exists_username(self, username: str) -> bool:
        return User.objects.filter(username=username).exists()

    def get_by_id(self, id: int) -> User | None:
        try:
            return User.objects.get(pk=id)
        except User.DoesNotExist:
            return None

    def get_by_email(self, email: str) -> User | None:
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            return None
