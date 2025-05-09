# Generated by Django 5.1.5 on 2025-03-29 10:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0003_tbl_deliveryagent'),
        ('Seller', '0004_tbl_stock'),
        ('User', '0011_remove_tbl_cart_booking_remove_tbl_cart_product_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_date', models.DateField(auto_now_add=True)),
                ('booking_amount', models.CharField(max_length=30)),
                ('booking_status', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_user')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_qty', models.IntegerField(default=1)),
                ('cart_status', models.IntegerField(default=0)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.tbl_booking')),
                ('deliveryagent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_deliveryagent')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Seller.tbl_product')),
            ],
        ),
    ]
