from django.core.management import BaseCommand

from app.accounts.models import User


class Command(BaseCommand):
    """
    테스트 커맨드
    """

    def add_arguments(self, parser):
        parser.add_argument('--test', type=str)

    def handle(self, *args, **options):
        _input = options.get('test')
        print(f'hello {_input}')
