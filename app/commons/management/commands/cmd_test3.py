from django.core.management import BaseCommand

from app.accounts.models import User


class Command(BaseCommand):
    """
    테스트 커맨드
    """

    def handle(self, *args, **options):
        from core.utils.secret_manager import load_secrets_manager_env
        load_secrets_manager_env()
