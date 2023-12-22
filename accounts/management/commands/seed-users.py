# Basic Django Modules
from django.core.management.base import BaseCommand

# Custom Models
from accounts.models import User

# faker
from faker import Faker


class Command(BaseCommand):
    help = "이 커맨드를 통해 랜덤한 테스트 유저 데이터를 만듭니다."

    def add_arguments(self, parser):
        parser.add_argument(
            "--total",
            default=2,
            type=int,
            help="몇 명의 유저를 만드나",
        )

    def handle(self, *args, **options):
        total = options.get("total")
        fake = Faker(["ko_KR"])

        for _ in range(total):
            # User 인스턴스 생성 및 저장
            user = User.objects.create(
                username=fake.user_name(),
                email=fake.email(),
                name=fake.name(),
                about_me=fake.catch_phrase(),
                school_name=fake.company(),
                nickname=fake.user_name(),
                grade=fake.random_int(min=1, max=3),
                is_staff=False,
                is_superuser=False,
            )
            user.set_password("1234")
            user.save()

        self.stdout.write(self.style.SUCCESS(f"{total}명의 유저가 작성되었습니다."))
