# Generated by Django 4.1.2 on 2022-10-23 20:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0001_initial'),
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymenttransaction',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AddField(
            model_name='ordering',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.customer'),
        ),
        migrations.AddField(
            model_name='ordering',
            name='payment_transaction',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='payment.paymenttransaction'),
        ),
        migrations.AddField(
            model_name='ordering',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product'),
        ),
    ]
