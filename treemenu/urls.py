from django.urls import path
from .views import menu

urlpatterns = [
    path('all/', menu, name='all'),
    path('byname/<str:menu_name>/', menu, name='byname')
]
