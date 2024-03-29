# Generated by Django 4.1.3 on 2023-08-06 19:11

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Task",
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
                    "type_publication",
                    models.CharField(
                        choices=[
                            ("page_publish", "page_publish"),
                            ("page_archive", "page_archive"),
                        ],
                        max_length=32,
                    ),
                ),
                ("object_id", models.IntegerField()),
                ("execution_date", models.DateTimeField()),
                ("retries", models.IntegerField(default=0)),
            ],
        ),
    ]
