# Generated by Django 3.1.2 on 2020-11-11 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20201110_1508'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={},
        ),
        migrations.AlterIndexTogether(
            name='product',
            index_together=set(),
        ),
    ]
