# Generated by Django 3.0.2 on 2020-03-21 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dormitories', '0008_auto_20200305_2205'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='waterfees',
            name='cost',
        ),
        migrations.RemoveField(
            model_name='waterfees',
            name='month',
        ),
        migrations.RemoveField(
            model_name='waterfees',
            name='surplus_water',
        ),
        migrations.RemoveField(
            model_name='waterfees',
            name='total_water',
        ),
        migrations.RemoveField(
            model_name='waterfees',
            name='used_water',
        ),
        migrations.AddField(
            model_name='waterfees',
            name='have_electricity_fees',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=5, verbose_name='现有金额(元)'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='electricityfees',
            name='dormitory',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='electricity_fees_s_dormitory', to='dormitories.Dormitory', verbose_name='宿舍'),
        ),
        migrations.AlterField(
            model_name='waterfees',
            name='dormitory',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='water_fees_s_dormitory', to='dormitories.Dormitory', verbose_name='宿舍'),
        ),
        migrations.AlterField(
            model_name='waterfees',
            name='note',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='备注'),
        ),
    ]
