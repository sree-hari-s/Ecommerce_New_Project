# Generated by Django 4.1.4 on 2022-12-24 07:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='test',
        ),
    ]
