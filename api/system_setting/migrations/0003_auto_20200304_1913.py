# Generated by Django 3.0.2 on 2020-03-04 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system_setting', '0002_auto_20200302_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='systemsetting',
            name='title',
            field=models.CharField(max_length=20, verbose_name='标题'),
        ),
    ]