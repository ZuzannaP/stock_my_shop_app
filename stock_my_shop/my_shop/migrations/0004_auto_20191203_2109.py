# Generated by Django 2.2.5 on 2019-12-03 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_shop', '0003_auto_20191203_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='vat',
            field=models.FloatField(choices=[(0.23, '0.23'), (0.08, '0.08'), (0.05, '0.05'), (0, '0')]),
        ),
    ]
