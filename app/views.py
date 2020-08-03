from django.shortcuts import render
from .models import Article


# 首页
def index(request):
    articles = Article.objects.all()[:5]
    return render(request, 'index.html', locals())


def map(request):
    return render(request, 'map.html', locals())


def article(request, article_id):
    try:
        article = Article.objects.get(pk=article_id)
        if article.isPublish == 0:
            raise Exception('该文章还没有发布，禁止访问！')
    except Exception as e:
        pass
    return render(request, 'article.html', locals())
