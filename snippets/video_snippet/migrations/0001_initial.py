# Generated by Django 4.1.3 on 2023-03-28 21:18

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("video", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="VideoSnippet",
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
                (
                    "videos",
                    models.ManyToManyField(blank=True, null=True, to="video.video"),
                ),
            ],
        ),
    ]
