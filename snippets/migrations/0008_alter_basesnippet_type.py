# Generated by Django 4.1.3 on 2024-04-16 21:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("snippets", "0007_delete_htmlsnippet"),
    ]

    operations = [
        migrations.AlterField(
            model_name="basesnippet",
            name="type",
            field=models.CharField(
                blank=True,
                choices=[
                    ("wyswig_snippet", "Wyswig"),
                    ("video_snippet", "Video"),
                    ("html_snippet", "HTML"),
                    ("header_snippet", "Header"),
                ],
                max_length=200,
                null=True,
            ),
        ),
    ]
