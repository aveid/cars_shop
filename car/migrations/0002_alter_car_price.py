# Generated by Django 4.1.4 on 2022-12-15 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("car", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car",
            name="price",
            field=models.DecimalField(decimal_places=10, max_digits=100),
        ),
    ]
