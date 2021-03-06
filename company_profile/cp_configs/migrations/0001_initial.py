# Generated by Django 2.1 on 2018-08-10 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BrandAssets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favicon', models.ImageField(blank=True, null=True, upload_to='cp/favicon')),
                ('hero_image_1', models.ImageField(blank=True, null=True, upload_to='cp/hero_image')),
                ('hero_image_2', models.ImageField(blank=True, null=True, upload_to='cp/hero_image')),
                ('hero_image_3', models.ImageField(blank=True, null=True, upload_to='cp/hero_image')),
                ('brand_logo', models.ImageField(blank=True, null=True, upload_to='cp/brand_logo')),
            ],
        ),
        migrations.CreateModel(
            name='BrandIdentity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(blank=True, max_length=250)),
                ('company_tagline', models.CharField(blank=True, max_length=350)),
                ('company_address', models.CharField(blank=True, max_length=450)),
                ('company_email_address', models.EmailField(blank=True, max_length=254, null=True)),
                ('company_phone_number', models.CharField(blank=True, max_length=35)),
                ('company_fax_number', models.CharField(blank=True, max_length=35)),
                ('company_facebook', models.CharField(blank=True, max_length=150)),
                ('company_instagram', models.CharField(blank=True, max_length=150)),
                ('company_whatsapp', models.CharField(blank=True, max_length=35)),
            ],
        ),
        migrations.CreateModel(
            name='ColorScheme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150)),
                ('primary_color', models.CharField(blank=True, max_length=6)),
                ('dark_color', models.CharField(blank=True, max_length=6)),
                ('accent_color', models.CharField(blank=True, max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Templates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150)),
                ('dir_name', models.CharField(blank=True, max_length=150)),
            ],
        ),
    ]
