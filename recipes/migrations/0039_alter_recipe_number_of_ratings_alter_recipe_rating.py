# Generated by Django 4.2.1 on 2024-04-27 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recipes", "0038_alter_recipe_ingredients_alter_recipe_preparation"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipe",
            name="number_of_ratings",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="recipe",
            name="rating",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
