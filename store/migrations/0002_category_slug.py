# Generated by Django 3.2.7 on 2023-01-07 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=0, max_length=100, unique=True),
            preserve_default=False,
        ),
    ]