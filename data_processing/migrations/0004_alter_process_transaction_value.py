# Generated by Django 4.1.5 on 2023-01-26 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("data_processing", "0003_alter_process_transaction_hour"),
    ]

    operations = [
        migrations.AlterField(
            model_name="process",
            name="transaction_value",
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
