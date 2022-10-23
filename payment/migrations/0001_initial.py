# Generated by Django 4.1.2 on 2022-10-23 20:56

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ordering',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Время изменения')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PaymentTransaction',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Время изменения')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('in', 'Ввод'), ('out', 'Вывод'), ('income', 'Доход'), ('reinvent', 'Реинвест'), ('income_ref', 'Реферальный доход'), ('income_from_partners', 'Доход от дохода Партнера')], default='in', max_length=100, verbose_name='Тип')),
                ('status', models.CharField(choices=[('new', 'Создана'), ('accepted', 'Подтверждена'), ('declined', 'Отклонена')], default='new', max_length=8, verbose_name='Статус')),
                ('value', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Значение')),
                ('wallet', models.CharField(blank=True, max_length=100, verbose_name='Кошелек')),
                ('data', models.JSONField(blank=True, verbose_name='Данные')),
            ],
            options={
                'verbose_name': 'Транзакция',
                'verbose_name_plural': 'Транзакции',
                'ordering': ('-created_at',),
            },
        ),
    ]
