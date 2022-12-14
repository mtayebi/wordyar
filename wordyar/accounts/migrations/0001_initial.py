# Generated by Django 4.1.1 on 2022-10-06 12:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='creat_time')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='update_time')),
                ('delete_time', models.DateTimeField(blank=True, null=True, verbose_name='delete_time')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='is_deleted')),
                ('level', models.CharField(choices=[('0', 'starter'), ('1', 'intermediate'), ('2', 'advanced'), ('3', 'legend')], default=None, max_length=1, null=True)),
                ('paid_user', models.BooleanField(default=False)),
                ('User', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'accounts',
                'verbose_name_plural': 'account',
            },
        ),
    ]
