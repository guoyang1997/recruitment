# Generated by Django 2.2.16 on 2020-10-29 11:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='创建日期'),
        ),
        migrations.AlterField(
            model_name='job',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='修改日期'),
        ),
    ]