# Generated by Django 3.0.2 on 2020-05-05 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20200505_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='captchamodel',
            name='email',
            field=models.EmailField(default=1, max_length=100, verbose_name='邮箱'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userface',
            name='features',
            field=models.TextField(null=True, verbose_name='特征数据'),
        ),
        migrations.AlterField(
            model_name='userface',
            name='photo',
            field=models.ImageField(null=True, upload_to='users/face_photo/', verbose_name='人脸照片'),
        ),
    ]
