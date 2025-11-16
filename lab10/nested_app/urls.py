from django.urls import path
from . import views

app_name = 'nested_app'

urlpatterns = [
    # Главная страница nested_app
    path('', views.index, name='index'),
    
    # Страница "О нас"
    path('about/', views.about, name='about'),
    
    # Страница контактов
    path('contact/', views.contact, name='contact'),
    
    # Детальная информация о товаре с параметром
    path('item/<int:item_id>/', views.item_detail, name='item_detail'),
]
