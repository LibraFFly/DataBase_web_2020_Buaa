# Generated by Django 3.1.3 on 2020-12-13 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_for_dbwork2', '0005_auto_20201213_1023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommend_item_route',
            name='hot',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='recommend_item_route',
            name='watch',
            field=models.IntegerField(),
        ),
    ]