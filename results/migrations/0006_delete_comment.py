# Generated by Django 4.2.7 on 2023-12-25 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0005_comment_delete_commentmodel'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]