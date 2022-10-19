from django.db import models
from django.contrib.auth import get_user_model
from shop.models import Product, Customer


User = get_user_model()


class Ordering(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date_of_ordering = models.DateTimeField(auto_now_add=True)
    # payment_transaction = must be True

    def __str__(self):
        return f"{self.product}"


class PaymentTransaction(models.Model):
     # some action
     pass


