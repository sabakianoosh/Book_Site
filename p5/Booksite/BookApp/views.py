
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Book, category


class IndexView(generic.ListView):
    template_name = 'BookApp/index.html'
    context_object_name = 'latest_Book_added'

    def get_queryset(self):
        """Return the last five Book added."""
        return Book.objects.order_by('-cover_image')[:5]
        

def book(request):
    context={'books' : Book.objects.all()}
    return render(request,'BookApp/book.html',context)
    
def add_book(request):
    if request.method == 'GET':
        return render(request,'BookApp/form.html')
    if request.method=="POST":
        data = request.POST
        Book.objects.create(title=data['title'],genre=data['genre'],author=data['author'],summary=data['summary'])
        return render(request,'BookApp/done.html')

def search(request):
    """ search function """
    if request.method == "POST":
        query_name = request.POST["title"]
        if query_name:
            results=Book.objects.filter(title__contains=query_name)
            return render(request,'BookApp/result.html',{"results":results})
    return render(request,'BookApp/search.html')


