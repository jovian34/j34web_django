# Generated by Django 4.0.6 on 2022-09-04 04:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iubase_players', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Photos',
            new_name='Photo',
        ),
        migrations.AlterField(
            model_name='transaction',
            name='date_announced',
            field=models.DateField(default=datetime.date(2022, 9, 4)),
        ),
    ]