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

    entries = util.list_entries()

    if title in entries:
        return render(request, "encyclopedia/wiki.html",
        {'title': title,
        'content': util.get_entry(title)  
        })    

    else:
        similars = [] 
        for entry in entries:
           if title in entry:
               similars.append(entry)

        return render(request, "encyclopedia/index.html", {
            "entries": similars
        })

def create_wiki(request):
    return render(request, "encyclopedia/create_wiki.html")
