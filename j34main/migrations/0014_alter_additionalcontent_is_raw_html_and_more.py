# Generated by Django 5.0.7 on 2024-07-13 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('j34main', '0013_alter_content_author_alter_content_image_caption_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='additionalcontent',
            name='is_raw_html',
            field=models.BooleanField(db_default=False),
        ),
        migrations.AlterField(
            model_name='content',
            name='author',
            field=models.CharField(db_default='Carl James', max_length=100),
        ),
        migrations.AlterField(
            model_name='content',
            name='image_caption',
            field=models.CharField(blank=True, db_default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='content',
            name='location',
            field=models.CharField(db_default='BLOOMINGTON, IN', max_length=100),
        ),
        migrations.AlterField(
            model_name='content',
            name='sub_title',
            field=models.CharField(blank=True, db_default='', max_length=100),
        ),
    ]
