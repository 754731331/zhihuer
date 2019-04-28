# Generated by Django 2.0.3 on 2018-06-16 14:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='回答内容')),
                ('pub_time',
                 models.DateTimeField(auto_now_add=True, verbose_name='发布时间')),
                ('author', models.ForeignKey(
                    on_delete=django.db.models.deletion.DO_NOTHING,
                    to=settings.AUTH_USER_MODEL, verbose_name='回答作者')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                (
                    'title',
                    models.CharField(max_length=200, verbose_name='问题标题')),
                ('content', models.TextField(verbose_name='问题内容')),
                ('pub_time',
                 models.DateTimeField(auto_now_add=True, verbose_name='发布时间')),
                ('recommend',
                 models.BooleanField(default=False, verbose_name='是否推荐')),
                ('read_nums',
                 models.IntegerField(default=0, verbose_name='阅读量')),
                ('author', models.ForeignKey(
                    on_delete=django.db.models.deletion.DO_NOTHING,
                    to=settings.AUTH_USER_MODEL, verbose_name='问题作者')),
            ],
            options={
                'ordering': ['-pub_time'],
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='话题')),
                ('add_time',
                 models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='topics',
            field=models.ManyToManyField(blank=True, to='zhihu.Topic',
                                         verbose_name='话题'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                to='zhihu.Question', verbose_name='回答问题'),
        ),
    ]
