# Generated by Django 5.0.6 on 2024-07-06 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("navbar", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="authors",
            name="first_name",
            field=models.CharField(max_length=50, verbose_name="Ism"),
        ),
        migrations.AlterField(
            model_name="authors",
            name="last_name",
            field=models.CharField(max_length=50, verbose_name="Familya"),
        ),
    ]
