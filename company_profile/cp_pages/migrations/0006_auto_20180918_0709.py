# Generated by Django 2.0.8 on 2018-09-18 07:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cp_pages', '0005_pagemodel_page_view'),
    ]

    operations = [
        migrations.CreateModel(
            name='TempPageModel',
            fields=[
                ('pagemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cp_pages.PageModel')),
            ],
            bases=('cp_pages.pagemodel',),
        ),
        migrations.AddField(
            model_name='pagemodel',
            name='class_name',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]