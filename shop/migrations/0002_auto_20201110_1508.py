# Generated by Django 3.1.2 on 2020-11-10 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ()},
        ),
        migrations.AlterIndexTogether(
            name='product',
            index_together={('id',)},
        ),
        migrations.RemoveField(
            model_name='product',
            name='name',
        ),
        migrations.RemoveField(
            model_name='product',
            name='slug',
        ),
    ]
