# Generated by Django 2.1.7 on 2019-03-13 02:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracks', '0006_like_track'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='track',
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]