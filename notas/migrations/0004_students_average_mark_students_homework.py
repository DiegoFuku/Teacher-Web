# Generated by Django 4.1.5 on 2023-01-28 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notas', '0003_rename_first_note_students_first_mark_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='average_mark',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='students',
            name='homework',
            field=models.FloatField(blank=True, null=True),
        ),
    ]