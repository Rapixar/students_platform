# Generated by Django 3.1.7 on 2021-03-27 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20210327_2143'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='id',
        ),
        migrations.AlterField(
            model_name='student',
            name='roll_no',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
