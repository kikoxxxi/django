# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-15 11:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Maker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('country', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='PModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('url', models.URLField(default='https://note.youdao.com/yws/public/resource/08345447630fc566479d74186c0cf507/xmlnote/WEBRESOURCEa62cb32ae78504929bf5138b992c2f9c/2647')),
                ('maker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.Maker')),
            ],
        ),
        migrations.CreateModel(
            name='PPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(default='\u4ea7\u54c1\u7167\u7247', max_length=20)),
                ('url', models.URLField(default='https://note.youdao.com/yws/public/resource/08345447630fc566479d74186c0cf507/xmlnote/WEBRESOURCEdbfaa126a02dfc98dc446e7718618051/2652')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(default='\u8d85\u503c\u4e8c\u624b\u624b\u673a', max_length=15)),
                ('description', models.TextField(default='\u6682\u65e0\u8bf4\u660e')),
                ('year', models.PositiveIntegerField(default=2016)),
                ('price', models.PositiveIntegerField(default=0)),
                ('pmodel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.PModel')),
            ],
        ),
        migrations.AddField(
            model_name='pphoto',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.Product'),
        ),
    ]