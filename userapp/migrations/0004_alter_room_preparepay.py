# Generated by Django 4.2.5 on 2023-10-06 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0003_rename_preparepay_savedrooms_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='preparePay',
            field=models.IntegerField(default=None, null=True),
        ),
    ]