from django.urls import path, include
from .views import NewUserViewSet, index, RegisterUser, LoginUser
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'users', NewUserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path(r'auth/', include('djoser.urls')),
    path('index/', index, name='home'),
    path('register', RegisterUser.as_view()),
    path('login/', LoginUser.as_view()),
]