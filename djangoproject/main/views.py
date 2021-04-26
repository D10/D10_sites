from django.shortcuts import render


def index(request):  # Функция, которая отвечает за вывод определенной страницы, при переходе по ее URL адресу
    data = {
        'title': 'Главная страница',
        'values': ['Some', 'Hello', '123'],
        'obj': {
            'car': 'BMW',
            'age': 18,
            'hobby': 'football'
        }
    }
    return render(request, 'main/index.html', data)


def about(request):  # Функция, которая отвечает за вывод определенной страницы, при переходе по ее URL адресу
    return render(request, 'main/about.html')
