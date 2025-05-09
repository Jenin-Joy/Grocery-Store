# Generated by Django 5.1.5 on 2025-02-19 06:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0003_tbl_deliveryagent'),
        ('Seller', '0004_tbl_stock'),
        ('User', '0004_delete_tbl_complaint'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint_subject', models.CharField(max_length=30)),
                ('complaint_complaint', models.CharField(max_length=30)),
                ('complaint_date', models.DateField(auto_now_add=True)),
                ('complaint_status', models.IntegerField(default=0)),
                ('complaint_reply', models.CharField(max_length=30)),
                ('complaint_replydate', models.DateField(null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Seller.tbl_product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_user')),
            ],
        ),
    ]
