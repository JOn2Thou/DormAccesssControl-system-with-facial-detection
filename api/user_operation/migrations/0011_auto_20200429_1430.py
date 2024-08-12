# Generated by Django 3.0.2 on 2020-04-29 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_operation', '0010_auto_20200428_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feesrechargeorder',
            name='recharge_type',
            field=models.CharField(choices=[('alipay', '支付宝'), ('qqpay', 'QQ钱包'), ('wechar', '微信')], default='alipay', max_length=6, verbose_name='充值方式'),
        ),
    ]