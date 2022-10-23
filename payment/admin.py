from django.contrib import admin
from .models import Ordering, PaymentTransaction


admin.site.register(Ordering)
admin.site.register(PaymentTransaction)

