# Generated by Django 3.1.3 on 2020-11-20 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0022_auto_20201119_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(to='news.tags'),
        ),
    ]