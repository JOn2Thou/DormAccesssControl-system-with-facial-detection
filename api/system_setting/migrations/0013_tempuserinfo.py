# Generated by Django 3.2 on 2023-07-07 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system_setting', '0012_auto_20200506_1326'),
    ]

    operations = [
        migrations.CreateModel(
            name='tempUserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=30)),
            ],
        ),
    ]