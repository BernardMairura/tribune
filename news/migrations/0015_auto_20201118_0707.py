# Generated by Django 3.1.3 on 2020-11-18 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0014_auto_20201118_0700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(to='news.tags'),
        ),
    ]
