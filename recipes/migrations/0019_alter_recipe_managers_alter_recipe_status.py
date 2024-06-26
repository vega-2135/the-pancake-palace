# Generated by Django 4.2.1 on 2024-04-07 21:26

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ("recipes", "0018_recipe_saved_recipes"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="recipe",
            managers=[
                ("newmanager", django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name="recipe",
            name="status",
            field=models.IntegerField(default=0),
        ),
    ]
