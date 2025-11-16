from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    """
    Главная страница nested_app
    """
    return HttpResponse('<h1>Welcome to Nested App!</h1>')
def about(request):
    """
    Страница "О нас"
    """
    return HttpResponse('<h1>About Nested App</h1><p>This is a nested application demonstrating URL routing with include().</p>')
def contact(request):
    """
    Страница контактов
    """
    return HttpResponse('<h1>Contact Us</h1><p>Email: contact@nestedapp.com</p>')
def item_detail(request, item_id):
    """
    Страница детальной информации о товаре
    """
    return HttpResponse(f'<h1>Item Detail</h1><p>You are viewing item #{item_id}</p>')

