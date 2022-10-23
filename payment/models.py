import uuid
from django.db import models
from django.contrib.auth import get_user_model
from shop.models import Product, Customer


User = get_user_model()


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Время изменения")

    class Meta:
        abstract = True


class Ordering(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='Покупатель')
    payment_transaction = models.OneToOneField('PaymentTransaction', on_delete=models.CASCADE, verbose_name='Транзакция')

    def __str__(self):
        return f"Заказ продукта - {self.product}"

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class PaymentTransaction(BaseModel):
    TYPES = (
        ('in', 'Ввод'),
        ('out', 'Вывод'),
        ('income', 'Доход'),
        ('reinvent', 'Реинвест'),
        ('income_ref', 'Реферальный доход'),
        ('income_from_partners', 'Доход от дохода Партнера'),
    )

    STATUSES = (
        ('new', 'Создана'),
        ('accepted', 'Подтверждена'),
        ('declined', 'Отклонена'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    type = models.CharField(max_length=100, choices=TYPES, default='in', verbose_name='Тип')
    status = models.CharField(max_length=8, choices=STATUSES, default='new', verbose_name='Статус')
    value = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Значение')
    wallet = models.CharField(max_length=100, blank=True, verbose_name='Кошелек')
    data = models.JSONField(blank=True, verbose_name='Данные')

    class Meta:
        verbose_name = 'Транзакция'
        verbose_name_plural = 'Транзакции'
        ordering = ('-created_at',)

    def __str__(self):
        return f'Транзакция пользователя - {self.user}'


