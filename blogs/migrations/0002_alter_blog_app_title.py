# Generated by Django 5.0.6 on 2024-07-07 16:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blogs", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog_app",
            name="title",
            field=models.CharField(max_length=25),
        ),
    ]
