# Generated by Django 3.0.6 on 2020-05-12 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('energy', '0013_auto_20200512_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='csv',
            field=models.FilePathField(blank=True),
        ),
        migrations.AlterField(
            model_name='result',
            name='graph',
            field=models.FilePathField(blank=True),
        ),
        migrations.AlterField(
            model_name='result',
            name='result',
            field=models.IntegerField(blank=True),
        ),
    ]
