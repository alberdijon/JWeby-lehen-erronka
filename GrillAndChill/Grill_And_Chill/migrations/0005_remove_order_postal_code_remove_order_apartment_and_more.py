# Generated by Django 5.1.1 on 2024-11-04 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Grill_And_Chill', '0004_alter_order_order_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='Postal_code',
        ),
        migrations.RemoveField(
            model_name='order',
            name='apartment',
        ),
        migrations.RemoveField(
            model_name='order',
            name='city',
        ),
        migrations.RemoveField(
            model_name='order',
            name='state',
        ),
        migrations.RemoveField(
            model_name='user',
            name='Postal_code',
        ),
        migrations.RemoveField(
            model_name='user',
            name='apartment',
        ),
        migrations.RemoveField(
            model_name='user',
            name='city',
        ),
        migrations.RemoveField(
            model_name='user',
            name='state',
        ),
    ]
