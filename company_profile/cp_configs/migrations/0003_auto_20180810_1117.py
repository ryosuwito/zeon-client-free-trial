# Generated by Django 2.1 on 2018-08-10 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cp_configs', '0002_auto_20180810_0956'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='brandasset',
            options={'verbose_name_plural': 'Brand Assets'},
        ),
        migrations.AlterModelOptions(
            name='brandidentity',
            options={'verbose_name_plural': 'Brand Identities'},
        ),
        migrations.AlterModelOptions(
            name='colorscheme',
            options={'verbose_name_plural': 'Color Schemes'},
        ),
    ]
