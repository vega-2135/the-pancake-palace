# Generated by Django 4.2.1 on 2024-04-26 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contact", "0003_alter_reachout_message"),
    ]

    operations = [
        migrations.CreateModel(
            name="ContactMe",
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
                ("title", models.CharField(max_length=200)),
                ("content", models.TextField()),
            ],
        ),
    ]