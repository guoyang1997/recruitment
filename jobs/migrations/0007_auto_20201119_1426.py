# Generated by Django 2.2.16 on 2020-11-19 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0006_auto_20201119_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='degree',
            field=models.SmallIntegerField(blank=True, choices=[(0, '本科'), (1, '硕士'), (2, '博士')], verbose_name='学历'),
        ),
    ]
