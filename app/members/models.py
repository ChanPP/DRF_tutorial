from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # AUTH_USER_MODEL 재정의
    # INSTALLED_APPS추가
    # DB삭제
    # Migrations삭제
    # 새로 makemigrations
    # migrate
    pass
