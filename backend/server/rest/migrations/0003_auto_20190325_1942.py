# Generated by Django 2.1.7 on 2019-03-25 19:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0002_auto_20190325_1939'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserContact',
            new_name='UserUser',
        ),
        migrations.AlterModelTable(
            name='useruser',
            table='user_user',
        ),
    ]