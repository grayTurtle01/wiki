from django.shortcuts import render

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

