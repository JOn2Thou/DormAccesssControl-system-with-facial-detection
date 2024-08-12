# Generated by Django 3.0.2 on 2020-03-17 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dormitories', '0008_auto_20200305_2205'),
        ('users', '0004_auto_20200313_1301'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='lived_dormitory',
        ),
        migrations.AddField(
            model_name='user',
            name='dormitory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_s_dormitory', to='dormitories.Dormitory', verbose_name='居住宿舍'),
        ),
    ]
