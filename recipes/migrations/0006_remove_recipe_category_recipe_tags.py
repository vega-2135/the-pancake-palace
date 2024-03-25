# Generated by Django 4.2.1 on 2024-03-25 15:06

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ("taggit", "0005_auto_20220424_2025"),
        ("recipes", "0005_alter_recipe_ingredients_alter_recipe_preparation"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="recipe",
            name="category",
        ),
        migrations.AddField(
            model_name="recipe",
            name="tags",
            field=taggit.managers.TaggableManager(
                blank=True,
                help_text="A comma-separated list of tags.",
                through="taggit.TaggedItem",
                to="taggit.Tag",
                verbose_name="Tags",
            ),
        ),
    ]
