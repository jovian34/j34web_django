# Generated by Django 4.1 on 2022-09-05 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "iubase_players",
            "0009_alter_academic_degree_level_alter_academic_major_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="transaction",
            name="draft_round",
            field=models.IntegerField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name="transaction",
            name="jersey",
            field=models.IntegerField(blank=True, default=None),
        ),
    ]
