# Generated by Django 4.1.4 on 2022-12-15 03:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("categories", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="modelcar",
            name="brand",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="models",
                to="categories.brand",
                verbose_name="Марка машины",
            ),
        ),
    ]
