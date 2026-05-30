from django.contrib.auth.backends import ModelBackend
from django.http import HttpRequest

from apps.user.models import User


class EmailBackend(ModelBackend):
    def authenticate(
        self,
        request: HttpRequest | None,
        username: str | None = None,
        password: str | None = None,
        **kwargs: object,
    ) -> User | None:
        email = kwargs.get("email") or username
        if not email or not password:
            return None
        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None
        return None
