# Generated by Django 2.1 on 2018-08-10 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('membership', '0005_member_site'),
        ('cp_configs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserConfigs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_assets', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cp_configs.BrandAssets')),
                ('brand_identity', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cp_configs.BrandIdentity')),
                ('color_scheme', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cp_configs.ColorScheme')),
                ('member', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='membership.Member')),
                ('templates', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cp_configs.Templates')),
            ],
        ),
    ]
