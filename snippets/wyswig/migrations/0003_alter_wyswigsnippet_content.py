# Generated by Django 4.1.3 on 2023-03-25 20:20

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("wyswig", "0002_alter_wyswigsnippet_content"),
    ]

    operations = [
        migrations.AlterField(
            model_name="wyswigsnippet",
            name="content",
            field=tinymce.models.HTMLField(default=None),
            preserve_default=False,
        ),
    ]
