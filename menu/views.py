from django.shortcuts import render
from .models import Category, Article


def home(request):
    return render(
        request, 'menu/home.html',
        {'categories': Category.objects.all()}
    )


def get_category(request, slug):
    category = Category.objects.get(slug=slug)
    

    return render(
        request, 'menu/category.html',
        {'category': category, 'categories': Category.objects.all()}
    )


def get_article(request, article_id):
    article = Article.objects.get(pk=article_id)
    return render(
        request, 'menu/article.html',
        {'article': article}
    )
