# Generated by Django 4.1 on 2023-05-21 07:57

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ("buy", "0002_admin_goods_order_orderinfo_shoppingcart_user_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="OrderView",
            fields=[
                (
                    "orderId",
                    models.CharField(max_length=30, primary_key=True, serialize=False),
                ),
                ("userName", models.CharField(max_length=10)),
                ("number", models.CharField(max_length=20)),
                ("address", models.CharField(max_length=40)),
                ("totalPrice", models.DecimalField(decimal_places=2, max_digits=7)),
                ("time", models.DateTimeField()),
            ],
            options={
                "db_table": "OrderView",
                "managed": False,
            },
            managers=[
                ("object", django.db.models.manager.Manager()),
            ],
        ),
    ]