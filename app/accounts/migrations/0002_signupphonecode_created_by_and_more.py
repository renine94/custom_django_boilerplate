# Generated by Django 4.1.6 on 2023-03-03 19:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="signupphonecode",
            name="created_by",
            field=models.CharField(
                default=None, max_length=50, null=True, verbose_name="생성한 사람"
            ),
        ),
        migrations.AddField(
            model_name="signupphonecode",
            name="updated_by",
            field=models.CharField(
                default=None, max_length=50, null=True, verbose_name="수정한 사람"
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="created_by",
            field=models.CharField(
                default=None, max_length=50, null=True, verbose_name="생성한 사람"
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="updated_by",
            field=models.CharField(
                default=None, max_length=50, null=True, verbose_name="수정한 사람"
            ),
        ),
    ]
