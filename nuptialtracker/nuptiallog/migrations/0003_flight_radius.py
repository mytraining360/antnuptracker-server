# Generated by Django 2.2.7 on 2020-05-14 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nuptiallog', '0002_auto_20200124_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='radius',
            field=models.FloatField(default=0.0, verbose_name='radius of location approximation (km)'),
        ),
    ]