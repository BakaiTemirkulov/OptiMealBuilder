# Generated by Django 4.2.7 on 2023-12-25 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SuccessStory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('before_photo', models.ImageField(upload_to='success_stories')),
                ('after_photo', models.ImageField(upload_to='success_stories')),
                ('description', models.TextField()),
            ],
        ),
    ]
