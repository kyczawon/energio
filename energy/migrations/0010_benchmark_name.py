# Generated by Django 3.0.6 on 2020-05-11 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('energy', '0009_auto_20200511_2030'),
    ]

    operations = [
        migrations.AddField(
            model_name='benchmark',
            name='name',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]