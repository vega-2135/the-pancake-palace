# Generated by Django 4.2.1 on 2024-04-11 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recipes", "0027_rename_publish_recipe_make_public"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipe",
            name="ingredients",
            field=models.JSONField(),
        ),
    ]
