# Generated by Django 2.2.16 on 2020-11-19 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_auto_20201118_1126'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='job',
            options={'verbose_name': '职位', 'verbose_name_plural': '职位'},
        ),
        migrations.AlterField(
            model_name='resume',
            name='degree',
            field=models.SmallIntegerField(blank=True, choices=[(0, '本科'), (1, '硕士'), (2, '博士')], max_length=135, verbose_name='学历'),
        ),
    ]