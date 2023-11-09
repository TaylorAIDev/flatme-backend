# Generated by Django 4.2.5 on 2023-10-06 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0005_alter_savedrooms_cost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flatmate',
            name='size',
        ),
        migrations.AddField(
            model_name='room',
            name='size',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='savedrooms',
            name='cost',
            field=models.IntegerField(default=None, null=True),
        ),
    ]
