from django.shortcuts import render, get_object_or_404
from .models import BlogAticles

# Create your views here.

def blog_title(request):
    blogs = BlogAticles.objects.all()
    return render(request, 'blog/title.html', {'blogs':blogs})


def blog_article(request, article_id):
    # article = BlogAticles.objects.get(id=article_id)
    article = get_object_or_404(BlogAticles,id=article_id)
    # publish = article.publish
    content = {'article':article, }
    return render(request, 'blog/content.html', content)


