# Generated by Django 4.1.4 on 2022-12-27 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0002_remove_cartitem_coupon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
