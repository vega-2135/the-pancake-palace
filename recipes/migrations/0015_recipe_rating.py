# Generated by Django 4.2.1 on 2024-04-03 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recipes", "0014_rename_recipe_post_comment_recipe"),
    ]

    operations = [
        migrations.AddField(
            model_name="recipe",
            name="rating",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]