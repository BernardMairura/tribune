# Generated by Django 3.1.3 on 2020-11-24 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0024_auto_20201120_1857'),
    ]

    operations = [
        migrations.CreateModel(
            name='MoringaMerch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
            ],
        ),
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(to='news.tags'),
        ),
    ]