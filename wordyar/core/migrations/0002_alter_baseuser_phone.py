# Generated by Django 4.1.1 on 2022-10-03 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseuser',
            name='phone',
            field=models.CharField(default=None, max_length=11, null=True, verbose_name='phone'),
        ),
    ]
