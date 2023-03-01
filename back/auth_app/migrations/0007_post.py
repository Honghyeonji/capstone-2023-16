# Generated by Django 4.1.5 on 2023-02-19 19:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0006_user_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='글 제목')),
                ('content', models.TextField(verbose_name='글 내용')),
                ('is_public', models.BooleanField(verbose_name='공개 여부')),
                ('is_deleted', models.BooleanField(verbose_name='글 삭제 여부')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='생성 시각')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='갱신 시각')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='글쓴이')),
            ],
        ),
    ]