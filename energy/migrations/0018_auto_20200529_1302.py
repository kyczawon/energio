# Generated by Django 3.0.6 on 2020-05-29 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('energy', '0017_auto_20200513_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='result',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
    ]
