# Generated by Django 3.0.2 on 2020-03-24 17:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('access_control', '0006_auto_20200324_1637'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accesscontrolabnormalapplication',
            name='application_person',
        ),
        migrations.RemoveField(
            model_name='accesscontrolabnormalapplication',
            name='note',
        ),
        migrations.AddField(
            model_name='accesscontrolabnormalapplication',
            name='reply',
            field=models.TextField(default=1, verbose_name='申请回复'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='accesscontrolabnormalapplication',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='申请时间'),
        ),
    ]