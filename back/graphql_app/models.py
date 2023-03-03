from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class MyUserManager(BaseUserManager):
    pass


class User(AbstractBaseUser):
    EMAIL = 'EM'
    SIGN_UP_METHOD_CHOICES = [
        (EMAIL, 'EMAIL'),
    ]
    USERNAME_FIELD = 'email'
    objects = MyUserManager()

    email = models.EmailField(verbose_name='유저의 이메일', unique=True)
    username = models.CharField(max_length=254, unique=True)
    signup_method = models.CharField(max_length=2, choices=SIGN_UP_METHOD_CHOICES, default=EMAIL)
    picture_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='생성 시각')
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name='갱신 시각')

    class Meta:
        db_table = 'users'


class EmailUser(models.Model):
    """Deprecated. `User` 모델을 사용하세요."""
    email = models.EmailField(verbose_name='유저의 이메일', unique=True)
    password = models.TextField(verbose_name='유저의 비밀번호')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='생성 시각')
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name='갱신 시각')

    class Meta:
        db_table = 'email_users'


class Post(models.Model):
    # TODO: Tag, Read count, Category 추가 필요
    title = models.TextField(verbose_name="글 제목")
    content = models.TextField(verbose_name="글 내용")
    user_id = models.ForeignKey(User,
                                verbose_name="글쓴이",
                                on_delete=models.CASCADE)  # TODO: 추후 Persona id 로 변경 필요
    is_public = models.BooleanField(verbose_name="공개 여부", default=True)
    is_deleted = models.BooleanField(verbose_name="글 삭제 여부", default=False)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='생성 시각', null=True)
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name='갱신 시각', null=True)


from django.db import models


class Persona(models.Model):
    class Gender(models.TextChoices):
        NONE = 'NO', '미입력'
        MALE = 'ML', '남성'
        FEMALE = 'FM', '여성'

    class AgeGroup(models.IntegerChoices):
        NONE = 0
        _10 = 1
        _20 = 2
        _30 = 3
        _40 = 4
        _50 = 5
        ELDER = 6

    user = models.ForeignKey('graphql_app.User', null=False, verbose_name='대상 사용자', on_delete=models.CASCADE,
                             db_column='user_id')
    nickname = models.CharField('닉네임', unique=True, max_length=20)
    introduction = models.TextField('소개', blank=True, default='자기 소개가 없습니다.')
    is_public = models.BooleanField('공개 여부', default=True)
    gender = models.CharField('성별', max_length=2, choices=Gender.choices, null=True, default=None)
    age_group = models.IntegerField('연령대', choices=AgeGroup.choices, null=True, default=None)
    job = models.CharField('직업', max_length=15, null=True, blank=True, default=None)
    is_certified = models.BooleanField('공인 여부', default=False)

    created_at = models.DateTimeField('생성 시각', auto_now_add=True)
    updated_at = models.DateTimeField('갱신 시각', auto_now=True)

    def __str__(self):
        return f"[{self.pk}] {self.user.id}:{self.nickname}"

    class Meta:
        db_table = 'personas'
        verbose_name = '구독 페르소나'
        verbose_name_plural = '구독 페르소나 목록'