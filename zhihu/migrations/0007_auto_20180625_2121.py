# Generated by Django 2.0.3 on 2018-06-25 21:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('zhihu', '0006_auto_20180622_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='content',
            field=models.TextField(blank=True, null=True, verbose_name='问题内容'),
        ),
    ]
