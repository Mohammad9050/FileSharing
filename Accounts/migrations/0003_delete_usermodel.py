# Generated by Django 4.1.4 on 2022-12-14 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0002_rename_max_size_usermodel_size_used'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserModel',
        ),
    ]
