# Generated by Django 4.2.1 on 2024-04-11 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recipes", "0029_alter_recipe_ingredients"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipe",
            name="ingredients",
            field=models.JSONField(),
        ),
    ]
