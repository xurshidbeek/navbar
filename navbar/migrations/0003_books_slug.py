# Generated by Django 5.0.6 on 2024-07-11 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("navbar", "0002_alter_authors_first_name_alter_authors_last_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="books",
            name="slug",
            field=models.SlugField(blank=True, max_length=200, unique=True),
        ),
    ]
