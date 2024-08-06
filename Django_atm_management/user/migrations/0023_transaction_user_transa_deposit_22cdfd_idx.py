# Generated by Django 5.0.7 on 2024-08-06 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0022_transaction_final_balance'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='transaction',
            index=models.Index(fields=['deposit_amount', 'withdraw_amount', 'transaction_type', 'get_balance', 'final_balance'], name='user_transa_deposit_22cdfd_idx'),
        ),
    ]