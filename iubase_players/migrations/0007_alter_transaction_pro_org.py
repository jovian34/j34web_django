# Generated by Django 4.1 on 2022-09-04 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iubase_players', '0006_alter_academic_degree_date_alter_article_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='pro_org',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
