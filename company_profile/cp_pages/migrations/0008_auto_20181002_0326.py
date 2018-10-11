# Generated by Django 2.0.8 on 2018-10-02 03:26

from django.db import migrations, models
import taggit_selectize.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('cp_pages', '0007_pagemodel_is_preview'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagemodel',
            name='meta_description',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='pagemodel',
            name='meta_keyword',
            field=taggit_selectize.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
