# Generated by Django 5.0.4 on 2024-07-15 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Movie",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=250)),
                ("year", models.IntegerField()),
                ("genre", models.CharField(max_length=250)),
                ("poster", models.CharField(max_length=2083)),
                ("plot", models.TextField()),
            ],
        ),
    ]
