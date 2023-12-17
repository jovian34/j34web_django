# Generated by Django 5.0 on 2023-12-17 14:44

import django.db.models.functions.datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('j34main', '0011_additionalcontent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='pub_date',
            field=models.DateTimeField(db_default=django.db.models.functions.datetime.Now(), verbose_name='date published'),
        ),
    ]
