# Generated by Django 2.0.8 on 2018-09-27 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cp_articles', '0003_auto_20180927_0453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ManyToManyField(blank=True, related_name='article_category', to='cp_articles.Category'),
        ),
    ]
