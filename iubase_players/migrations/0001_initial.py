# Generated by Django 4.0.6 on 2022-09-04 03:54

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=100)),
                ('middle', models.CharField(max_length=100)),
                ('last', models.CharField(max_length=100)),
                ('hometown', models.CharField(max_length=100)),
                ('birthdate', models.DateField()),
                ('height', models.FloatField()),
                ('weight', models.FloatField()),
                ('bats', models.CharField(max_length=1)),
                ('throws', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SocialPlatform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('league', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iubase_players.league')),
            ],
        ),
        migrations.CreateModel(
            name='TransactionType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_announced', models.DateField(default=datetime.date(2022, 9, 3))),
                ('year', models.IntegerField()),
                ('season', models.CharField(max_length=10)),
                ('jersey', models.IntegerField()),
                ('draft_round', models.IntegerField()),
                ('pro_org', models.CharField(max_length=100)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iubase_players.player')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iubase_players.position')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iubase_players.team')),
                ('trans_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iubase_players.transactiontype')),
            ],
        ),
        migrations.CreateModel(
            name='TeamSocial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('handle', models.CharField(max_length=100)),
                ('platform', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iubase_players.socialplatform')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iubase_players.team')),
            ],
        ),
        migrations.CreateModel(
            name='PlayerSocial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('handle', models.CharField(max_length=100)),
                ('platform', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iubase_players.socialplatform')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iubase_players.player')),
            ],
        ),
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('date', models.DateField()),
                ('description', models.CharField(max_length=100)),
                ('credit', models.CharField(max_length=100)),
                ('player', models.ManyToManyField(to='iubase_players.player')),
            ],
        ),
        migrations.AddField(
            model_name='league',
            name='level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iubase_players.level'),
        ),
        migrations.CreateModel(
            name='Headshot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('date', models.DateField()),
                ('player', models.ManyToManyField(to='iubase_players.player')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('url', models.URLField()),
                ('publication', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('player', models.ManyToManyField(to='iubase_players.player')),
            ],
        ),
        migrations.CreateModel(
            name='Accolade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
                ('organization', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('season', models.CharField(max_length=10)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iubase_players.player')),
            ],
        ),
        migrations.CreateModel(
            name='Academic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree_date', models.DateField()),
                ('degree_level', models.CharField(max_length=100)),
                ('major', models.CharField(max_length=100)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iubase_players.player')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iubase_players.team')),
            ],
        ),
    ]
