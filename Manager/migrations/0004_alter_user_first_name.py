# Generated by Django 4.0.2 on 2022-05-15 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0003_alter_comment_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
