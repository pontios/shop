# Generated by Django 2.1.5 on 2019-01-13 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20190113_1325'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='accepted',
            field=models.BooleanField(default=True, verbose_name='Наличие'),
        ),
    ]