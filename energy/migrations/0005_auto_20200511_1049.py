# Generated by Django 3.0.6 on 2020-05-11 10:49

from django.db import migrations, models
import energy.models


class Migration(migrations.Migration):

    dependencies = [
        ('energy', '0004_auto_20200505_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='benchmark',
            name='category',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='benchmark',
            name='file',
            field=models.FileField(blank=True, upload_to='files/%Y/%m/%d', validators=[energy.models.validate_file_extension]),
        ),
    ]