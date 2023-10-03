from django.shortcuts import render, get_object_or_404
from .models import Article

# Create your views here.


def news(request):
    articles = Article.objects.all().order_by('-created')
    context = {'articles': articles}
    return render(request, 'articles/news_board.html', context)


def current_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    context = {
        'article': article,
    }
    return render(request, 'articles/article_details.html', context)
