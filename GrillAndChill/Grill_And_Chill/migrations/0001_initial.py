import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alergen',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('price', models.FloatField()),
                ('order_Date', models.DateField(auto_now=True)),
                ('ordered', models.FloatField()),
                ('ended', models.BooleanField(default=False)),
                ('direction', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=75)),
                ('surname', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('gmail', models.EmailField(max_length=100)),
                ('tlf', models.IntegerField()),
                ('direction', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=75)),
                ('description', models.CharField(max_length=100)),
                ('ingredients', models.CharField(max_length=1000)),
                ('price', models.FloatField(max_length=6)),
                ('foto', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Grill_And_Chill.category')),
            ],
        ),
        migrations.CreateModel(
            name='Product_Alergen',
            fields=[
                ('code', models.AutoField(primary_key=True, serialize=False)),
                ('alergens_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Grill_And_Chill.alergen')),
                ('products_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Grill_And_Chill.product')),
            ],
        ),
        migrations.CreateModel(
            name='Product_Order',
            fields=[
                ('code', models.AutoField(primary_key=True, serialize=False)),
                ('order_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Grill_And_Chill.order')),
                ('products_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Grill_And_Chill.product')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='user_Id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Grill_And_Chill.user'),
        ),
    ]
