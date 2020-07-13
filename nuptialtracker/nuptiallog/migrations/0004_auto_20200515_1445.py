# Generated by Django 2.2.7 on 2020-05-15 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nuptiallog', '0003_flight_radius'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flightuser',
            name='role',
        ),
        migrations.AddField(
            model_name='flightuser',
            name='description',
            field=models.TextField(blank=True, verbose_name='Public description'),
        ),
        migrations.AddField(
            model_name='flightuser',
            name='institution',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AddField(
            model_name='flightuser',
            name='professional',
            field=models.BooleanField(default=False),
        ),
    ]