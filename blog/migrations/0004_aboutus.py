# Generated by Django 4.2.7 on 2023-11-29 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_food_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('history', models.TextField(blank=True, null=True)),
                ('mission', models.TextField(blank=True, null=True)),
                ('values', models.TextField(blank=True, null=True)),
                ('team', models.TextField(blank=True, null=True)),
                ('contact_info', models.TextField(blank=True, null=True)),
                ('achievements', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
