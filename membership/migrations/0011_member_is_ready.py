# Generated by Django 2.0.8 on 2018-11-14 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0010_auto_20181010_1835'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='is_ready',
            field=models.BooleanField(default=False),
        ),
    ]
