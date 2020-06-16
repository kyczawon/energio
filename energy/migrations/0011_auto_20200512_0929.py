# Generated by Django 3.0.6 on 2020-05-12 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('energy', '0010_benchmark_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='benchmark',
            name='completed',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='benchmark',
            name='is_started',
            field=models.BooleanField(default=False),
        ),
    ]
