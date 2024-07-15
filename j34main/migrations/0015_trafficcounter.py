# Generated by Django 5.0.7 on 2024-07-15 16:33

import django.db.models.functions.datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('j34main', '0014_alter_additionalcontent_is_raw_html_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrafficCounter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page', models.CharField(max_length=128)),
                ('timestamp', models.DateTimeField(db_default=django.db.models.functions.datetime.Now())),
                ('ip', models.CharField(max_length=64, null=True)),
                ('user_agent', models.CharField(max_length=256, null=True)),
            ],
        ),
    ]
