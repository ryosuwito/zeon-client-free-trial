# Generated by Django 2.0.8 on 2018-11-14 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cp_configs', '0011_brandidentity_head_scripts'),
    ]

    operations = [
        migrations.RenameField(
            model_name='brandidentity',
            old_name='head_scripts',
            new_name='ads_scripts',
        ),
        migrations.AddField(
            model_name='brandidentity',
            name='other_scripts',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='brandidentity',
            name='tracking_scripts',
            field=models.TextField(blank=True),
        ),
    ]
