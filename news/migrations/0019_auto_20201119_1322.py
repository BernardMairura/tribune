# Generated by Django 3.1.3 on 2020-11-19 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0018_auto_20201119_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(to='news.tags'),
        ),
    ]