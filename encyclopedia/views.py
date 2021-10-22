from django.shortcuts import render, redirect
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

def save_wiki(request):
    title = request.GET['title']
    content = request.GET['content']

    entries = util.list_entries()

    if title in entries:
        return render(request, "encyclopedia/error.html", 
            {'message': 'That Wiki Title Already Exists'})

    # save the new page
    else:    
        util.save_entry(title, content)
        # return redirect('index')
        return redirect(f'/wiki/{title}')

def edit_wiki(request, title):
    content = util.get_entry(title)

    return render(request, 'encyclopedia/edit_wiki.html', {
        'title': title,
        'content': content
    })

def update_wiki(request, title):
    # title = request.GET['title']
    new_content = request.GET['content']

    util.save_entry(title, new_content)

    return redirect(f"/wiki/{title}")

import random
def random_wiki(request):
    entries = util.list_entries()

    index = random.randint(0, len(entries)-1 )
    title = entries[index]

    return redirect(f"/wiki/{title}")