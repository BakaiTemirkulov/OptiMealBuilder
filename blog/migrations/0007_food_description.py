# Generated by Django 4.2.7 on 2023-12-10 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_food_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]