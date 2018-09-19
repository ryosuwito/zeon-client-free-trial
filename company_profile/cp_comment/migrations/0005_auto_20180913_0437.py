# Generated by Django 2.0.8 on 2018-09-13 04:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cp_comment', '0004_auto_20180913_0435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2018, 9, 13, 4, 37, 2, 470678, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='reply',
            name='created_date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2018, 9, 13, 4, 37, 2, 471306, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='created_date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2018, 9, 13, 4, 37, 2, 470122, tzinfo=utc)),
        ),
    ]
