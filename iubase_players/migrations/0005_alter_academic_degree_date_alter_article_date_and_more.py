# Generated by Django 4.1 on 2022-09-04 18:09

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('iubase_players', '0004_player_country_player_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academic',
            name='degree_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='headshot',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='player',
            name='bats',
            field=models.CharField(max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='birthdate',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='country',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='height',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='hometown',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='middle',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='state',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='throws',
            field=models.CharField(max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='weight',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='playersocial',
            name='handle',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='state',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='teamsocial',
            name='handle',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='draft_round',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='jersey',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='position',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='iubase_players.position'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='iubase_players.team'),
        ),
    ]
