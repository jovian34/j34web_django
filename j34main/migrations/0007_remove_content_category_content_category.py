# Generated by Django 4.0.6 on 2022-07-16 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("j34main", "0006_content_category"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="content",
            name="category",
        ),
        migrations.AddField(
            model_name="content",
            name="category",
            field=models.ManyToManyField(default=2, to="j34main.category"),
        ),
    ]
