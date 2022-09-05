# Generated by Django 4.1 on 2022-09-05 00:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('iubase_players', '0012_alter_transaction_jersey'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accolade',
            name='season',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iubase_players.season'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='season',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iubase_players.season'),
        ),
    ]
