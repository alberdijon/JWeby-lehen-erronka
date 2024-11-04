# Generated by Django 5.1.1 on 2024-10-28 08:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Grill_And_Chill', '0002_category_rename_orders_order_product_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='products_Id',
        ),
        migrations.CreateModel(
            name='Product_Order',
            fields=[
                ('code', models.AutoField(primary_key=True, serialize=False)),
                ('order_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Grill_And_Chill.order')),
                ('products_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Grill_And_Chill.product')),
            ],
        ),
    ]
