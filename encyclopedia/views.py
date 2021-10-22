from django.shortcuts import render
from django.http import HttpResponse

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def wiki(request):
    return render(request, "encyclopedia/wiki.html")

def show_wiki(request, title):
    content = util.get_entry(title)

    return render(request, "encyclopedia/wiki.html",
     {'title': title,
      'content': util.get_entry(title)  
     })

def search_wiki(request):
    title = request.GET['q']

    return render(request, "encyclopedia/wiki.html",
     {'title': title,
      'content': util.get_entry(title)  
     })    
