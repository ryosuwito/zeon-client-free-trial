# Generated by Django 2.0.8 on 2018-11-14 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cp_configs', '0012_auto_20181114_1929'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brandidentity',
            name='meta_og_image',
        ),
    ]