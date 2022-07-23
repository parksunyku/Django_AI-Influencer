# Generated by Django 4.0.6 on 2022-07-23 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0006_bookmark_like_reply'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookmark',
            old_name='content_id',
            new_name='feed_id',
        ),
        migrations.AlterField(
            model_name='bookmark',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='feed',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='like',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
    ]
