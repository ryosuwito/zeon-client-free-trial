# Generated by Django 2.0.8 on 2018-09-13 04:42

import company_profile.cp_comment.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cp_comment', '0006_auto_20180913_0441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='created_date',
            field=models.DateTimeField(db_index=True, default=company_profile.cp_comment.models.default_now),
        ),
    ]
