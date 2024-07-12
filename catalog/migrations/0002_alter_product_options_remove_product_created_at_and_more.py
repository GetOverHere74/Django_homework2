# Generated by Django 5.0.6 on 2024-07-10 11:31

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={
                "ordering": ["manufactured_at"],
                "verbose_name": "Товар",
                "verbose_name_plural": "Товары",
            },
        ),
        migrations.RemoveField(
            model_name="product",
            name="created_at",
        ),
        migrations.AddField(
            model_name="product",
            name="manufactured_at",
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                verbose_name="Дата производства продукта",
            ),
            preserve_default=False,
        ),
    ]
