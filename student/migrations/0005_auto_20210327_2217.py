# Generated by Django 3.1.7 on 2021-03-27 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_auto_20210327_2213'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='id',
        ),
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.TextField(max_length=20),
        ),
    ]