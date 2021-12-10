# Generated by Django 4.0 on 2021-12-09 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookAuthor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('author', models.CharField(max_length=100)),
                ('read', models.CharField(max_length=3)),
            ],
        ),
    ]
