# Generated by Django 2.1.5 on 2019-01-14 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20190113_1543'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='accepted',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='item',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='total',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='user',
        ),
        migrations.AddField(
            model_name='cart',
            name='card_id',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='cart',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='shop.Cart'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]
