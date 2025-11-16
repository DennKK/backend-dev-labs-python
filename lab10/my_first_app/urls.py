from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_world, name='hello'),
    
    path('hello/<str:name>/', views.hello_world, name='hello_with_name'),

    path('redirect/', views.redirect_example, name='redirect'),
    
    path('json/', views.json_example, name='json'),
    
    path('cookies/', views.show_cookies, name='show_cookies'),
]
