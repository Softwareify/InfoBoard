# Generated by Django 4.1.3 on 2023-02-01 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("page", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="page",
            name="name",
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]
