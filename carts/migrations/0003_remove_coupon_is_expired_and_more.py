# Generated by Django 4.1.4 on 2022-12-28 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0002_cartitem_coupon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coupon',
            name='is_expired',
        ),
        migrations.RemoveField(
            model_name='coupon',
            name='minimum_amount',
        ),
    ]
