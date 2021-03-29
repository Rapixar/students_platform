# Generated by Django 3.1.7 on 2021-03-27 21:43

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('division', models.TextField()),
                ('name', models.TextField(max_length=20)),
                ('importance', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='dateOfBirth',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date of Birth'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='student',
            name='roll_no',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='stud_class',
            field=models.CharField(max_length=20, verbose_name="Student's class"),
        ),
        migrations.AlterField(
            model_name='student',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.department'),
        ),
    ]