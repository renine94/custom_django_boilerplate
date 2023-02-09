# Generated by Django 4.1.6 on 2023-02-09 03:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("boards", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="article",
            options={"verbose_name_plural": "게시글"},
        ),
        migrations.AlterModelOptions(
            name="comment",
            options={"verbose_name_plural": "댓글"},
        ),
        migrations.AlterField(
            model_name="article",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, verbose_name="생성일"),
        ),
        migrations.AlterField(
            model_name="article",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, verbose_name="수정일"),
        ),
        migrations.AlterField(
            model_name="comment",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, verbose_name="생성일"),
        ),
        migrations.AlterField(
            model_name="comment",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, verbose_name="수정일"),
        ),
    ]
