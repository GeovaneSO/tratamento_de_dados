# Generated by Django 4.1.5 on 2023-01-26 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("data_processing", "0004_alter_process_transaction_value"),
    ]

    operations = [
        migrations.AlterField(
            model_name="process",
            name="transaction_value",
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]
