from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required, login_required
from django.http import HttpResponse
from .models import Article

@permission_required('advanced_features_and_security.can_view', raise_exception=True)
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'advanced_features_and_security/article_list.html', {'articles': articles})

@permission_required('advanced_features_and_security.can_create', raise_exception=True)
def article_create(request):
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        content = request.POST.get('content', '').strip()
        if title and content:
            Article.objects.create(title=title, content=content, author=request.user)
            return redirect('afs:article_list')
    return render(request, 'advanced_features_and_security/article_form.html', {'action': 'Create'})

@permission_required('advanced_features_and_security.can_edit', raise_exception=True)
def article_edit(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        article.title = request.POST.get('title', article.title)
        article.content = request.POST.get('content', article.content)
        article.save()
        return redirect('afs:article_list')
    return render(request, 'advanced_features_and_security/article_form.html', {'action': 'Edit', 'article': article})

@permission_required('advanced_features_and_security.can_delete', raise_exception=True)
def article_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('afs:article_list')
    return render(request, 'advanced_features_and_security/article_confirm_delete.html', {'article': article})

