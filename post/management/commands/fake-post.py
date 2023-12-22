# Basic Django Modules
from django.core.management.base import BaseCommand
from django_seed import Seed

# Custom Models
from accounts.models import User
from post.models import Post, Comment, Like

# faker
from faker import Faker


class Command(BaseCommand):
    help = "이 커맨드를 통해 랜덤한 테스트 자유게시판 데이터를 만듭니다."

    def add_arguments(self, parser):
        parser.add_argument(
            "--total",
            default=2,
            type=int,
            help="몇 개의 게시글을 만드나",
        )

    def handle(self, *args, **options):
        total = options.get("total")
        users = User.objects.all()  # 모든 사용자 가져오기
        fake = Faker(["ko_KR"])

        for _ in range(total):
            # Post 인스턴스 생성 및 저장
            Post.objects.create(
                title=fake.catch_phrase(),
                content=fake.catch_phrase(),
                author=fake.random_element(users),
                is_notice=fake.boolean(chance_of_getting_true=20),
            )
        self.stdout.write(self.style.SUCCESS(f"{total}개의 자유게시판 데이터가 작성되었습니다."))
