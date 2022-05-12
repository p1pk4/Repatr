from django.shortcuts import render


def index(request):
    # data = {
    #     'title': 'Главная страница о репатриации!',
    #     'values': ['Some', 'Hello', '123'],
    #     'obj': {
    #         'car': 'BMW',
    #         'age': 18,
    #         'hobby': 'soccer'
    #     }
    # }
    return render(request, 'main/index.html',)  # data)


def all_info(request):
    return render(request, 'main/all_info.html')





def about(request):
    return render(request, 'main/about.html')
