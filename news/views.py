from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView


def news_home(request):
    # news = Articles.objects.all()
    news = Articles.objects.order_by('-id')  # Сортировка по названия в обратном порядке(-)
    return render(request, 'news/news_home.html', {'news': news})


def house(request):
    news = Articles.objects.order_by('-id')
    return render(request, 'news/house.html', {'news': news})


def documents(request):
    news = Articles.objects.order_by('-id')
    return render(request, 'news/documents.html', {'news': news})


def kids(request):
    news = Articles.objects.order_by('-id')
    return render(request, 'news/kids.html', {'news': news})


def money(request):
    news = Articles.objects.order_by('-id')
    return render(request, 'news/money.html', {'news': news})


def animals(request):
    news = Articles.objects.order_by('-id')
    return render(request, 'news/animals.html', {'news': news})


def israel(request):
    news = Articles.objects.order_by('-id')
    return render(request, 'news/israel.html', {'news': news})


class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'


class NewsDetailUpdateView(UpdateView):
    model = Articles
    template_name = 'news/update_news.html'

    form_class = ArticlesForm


class NewsDetailDeleteView(DeleteView):
    model = Articles

    success_url = '/news/'
    template_name = 'news/delete_news.html'


def create_news(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Форма заполнена неверно'

    form = ArticlesForm()

    data = {
        'form': form,
        'error': error

    }

    return render(request, 'news/create_news.html', data)
