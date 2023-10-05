from django.shortcuts import render
from .models import Category, Article

def home(request):
    return render(
        request, 'menu/home.html',
        {'categories': Category.objects.all()}
    )


def get_category(request, slug):
    category = Category.objects.get(slug=slug)
    # articles = Article.objects.filter(category__slug=slug)

    # print(articles)
    
    # следующий родственный элемент
    next_sibling = category.get_next_sibling()
    print(next_sibling)

    # предки
    # ancestors = category.get_ancestors(ascending=False, include_self=False)
    # print(ancestors)

    # непосредственные потомки
    # children = category.get_children()
    # print(children)
    
    # потомки
    # descendants = category.get_descendants()
    # print(descendants)

    # предки + текущая модель + потомки
    # family = category.get_family()
    # print(family)


    return render(
        request, 'menu/category.html',
        {'category': category, 'categories': Category.objects.all()}
    )