from django.urls import path
from . import views

urlpatterns = [
    #http://127.0.0.1:8000/dogs/1
    path('dogs/<int:id>', views.dog, name="dog"),

    #http://127.0.0.1:8000/dogs/
    path('dogs/', views.dogs),

    # http://127.0.0.1:8000/calc/add/1/1
    # http://127.0.0.1:8000/calc/sub/5/3
    # http://127.0.0.1:8000/calc/mul/3/10
    # http://127.0.0.1:8000/calc/div/12/4
    path('calc/<dzialanie>/<int:a>/<int:b>', views.calculator),

    # http://127.0.0.1:8000/texts/abcdsdfsdf
    path('texts/<int:ile_gwiazdek>/<user_text>', views.cool_text),
    # http://127.0.0.1:8000/hello/Konrad
    path('hello/<imie>', views.hello),
    path('about', views.about),
    path('', views.index)
]