# Generated by Django 3.0.6 on 2020-06-03 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('energy', '0019_auto_20200603_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='benchmark',
            name='exec_prog',
            field=models.CharField(choices=[('monkeyrunner', 'monkeyrunner'), ('java', 'Java 1.8.0_241-b07 (UI Automator)'), ('python', 'python 2.7.16 (androidViewClient)'), ('python3', 'python 3.7.4')], default='monkeyrunner', max_length=12),
        ),
    ]
