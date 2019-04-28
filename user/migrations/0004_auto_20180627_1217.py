# Generated by Django 2.0.3 on 2018-06-27 12:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('user', '0003_checkcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkcode',
            name='add_time',
            field=models.DateTimeField(auto_now=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=True,
                                   verbose_name='居住地'),
        ),
    ]
