# Generated by Django 5.0.8 on 2024-11-07 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sentirseBien', '0009_appointment_payment_deadline'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='discount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=2),
        ),
    ]
