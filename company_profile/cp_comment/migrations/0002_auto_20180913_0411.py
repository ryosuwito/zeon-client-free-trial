# Generated by Django 2.0.8 on 2018-09-13 04:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cp_comment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='reply',
            name='created_date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='visitor',
            name='created_date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime.now),
        ),
    ]
