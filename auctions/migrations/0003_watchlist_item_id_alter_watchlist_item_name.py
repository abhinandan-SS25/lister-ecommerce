# Generated by Django 4.0 on 2022-02-26 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_alter_comment_com_on_alter_comment_listing_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchlist',
            name='item_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='watchlist',
            name='item_name',
            field=models.CharField(max_length=300),
        ),
    ]
