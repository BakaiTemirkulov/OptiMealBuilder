# Generated by Django 4.2.7 on 2023-12-25 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0007_commentmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commentmodel',
            old_name='choice_film',
            new_name='choice_story',
        ),
    ]