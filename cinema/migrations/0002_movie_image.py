# Generated by Django 4.1 on 2024-04-27 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cinema", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="movie",
            name="image",
            field=models.ImageField(null=True, upload_to="create_custom_path"),
        ),
    ]
