from django.shortcuts import render
from .models import Ordering


def index(request, pk):
    queryset = Ordering.objects.get(pk=pk)

    return render(request, "payment/index.html", context={'Hi': "HELLO", 'order': queryset})