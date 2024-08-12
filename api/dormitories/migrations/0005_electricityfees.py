# Generated by Django 3.0.2 on 2020-03-04 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dormitories', '0004_waterrate_cost'),
    ]

    operations = [
        migrations.CreateModel(
            name='ElectricityFees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('have_electricity_fees', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='现有金额(元)')),
                ('dormitory', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='electricity_fees_dormitory', to='dormitories.Dormitory', verbose_name='宿舍')),
            ],
            options={
                'verbose_name': '宿舍电费',
                'verbose_name_plural': '宿舍电费',
            },
        ),
    ]
