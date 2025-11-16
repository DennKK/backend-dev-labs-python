from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse


def hello_world(request, name=None):
    """
    Представление hello_world с поддержкой параметра name из URL
    и параметра age из строки запроса
    """
    # Получаем параметр age из строки запроса
    age = request.GET.get('age', None)
    
    if name and age:
        response = HttpResponse(f'<h1>Hello, {name}! You are {age} years old.</h1>')
    elif name:
        response = HttpResponse(f'<h1>Hello, {name}!</h1>')
    else:
        response = HttpResponse('<h1>Hello, World!</h1>')

    if name:
        response.set_cookie('username', name)
    
    return response


def redirect_example(request):
    """
    Представление, которое перенаправляет на hello_world с параметрами по умолчанию
    """
    return redirect('hello_with_name', name='Guest')


def json_example(request):
    """
    Представление, возвращающее JSON-ответ с данными о пользователе
    """
    user_data = {
        'name': 'John Doe',
        'age': 25,
        'email': 'john.doe@example.com',
        'occupation': 'Software Developer'
    }
    return JsonResponse(user_data)


def show_cookies(request):
    """
    Представление, которое отображает все куки
    """
    cookies = request.COOKIES
    
    if cookies:
        cookies_html = '<ul>'
        for key, value in cookies.items():
            cookies_html += f'<li><strong>{key}:</strong> {value}</li>'
        cookies_html += '</ul>'
        return HttpResponse(f'<h1>Cookies:</h1>{cookies_html}')
    else:
        return HttpResponse('<h1>No cookies found</h1>')
