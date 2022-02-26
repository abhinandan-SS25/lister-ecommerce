# Generated by Django 4.0 on 2022-02-26 05:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='com_on',
            field=models.DateTimeField(default=datetime.date(2022, 2, 26)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='listing',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='listing',
            name='listing_open_date',
            field=models.DateField(default=datetime.date(2022, 2, 26)),
        ),
        migrations.AlterField(
            model_name='watchlist',
            name='item_name',
            field=models.IntegerField(),
        ),
    ]