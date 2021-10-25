from django.shortcuts import render, redirect
from django.http import HttpResponse
from django import forms

from . import util
from markdown2 import Markdown
import random




def index(request):
    entries = util.list_entries()
    print(entries)

    return render(request, "encyclopedia/index.html", {
        "entries": entries
    })
    

def wiki(request):
    return render(request, "encyclopedia/wiki.html")


def show_wiki(request, title):
    entries = util.list_entries()

    if title in entries:
        content = util.get_entry(title)
        # content = markdown2.markdown(content)
        markdowner = Markdown()
        content = markdowner.convert(content)

        return render(request, "encyclopedia/wiki.html",
        {'title': title,
        'content': content,
        #    'entries': util.list_entries()
        })
    else:
        return render(request, 'encyclopedia/error.html', {
            'message': f'Page: wiki/{title} doesn\'t Exist' 
            })

def search_wiki(request):
    title = request.GET['q']

    entries = util.list_entries()

    if title in entries:
        content = util.get_entry(title) 
        markdowner = Markdown()
        content = markdowner.convert(content)

        return render(request, "encyclopedia/wiki.html",
        {'title': title,
        'content': content,
        'entries': entries 
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

    entries = util.list_entries()


    if request.method == 'GET':
        return render(request, "encyclopedia/create_wiki.html",{
            'entries': entries,
        })

    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']

        if title == '':
            return render(request, "encyclopedia/error.html", 
                {'message': 'The Page Must Have Title'})


        if title in entries:
            return render(request, "encyclopedia/error.html", 
                {'message': 'That Page Title Already Exists'})

        # save the new page
        else:    
            util.save_entry(title, content)
            return redirect(f'/wiki/{title}')

def edit_wiki(request, title):

    if request.method == 'GET':
        content = util.get_entry(title)

        return render(request, 'encyclopedia/edit_wiki.html', {
            'title': title,
            'content': content,
             "entries": util.list_entries()
        })

    if request.method == 'POST':
        new_content = request.POST['content']

        util.save_entry(title, new_content)

        return redirect(f"/wiki/{title}")


def random_wiki(request):
    entries = util.list_entries()

    index = random.randint(0, len(entries)-1 )
    title = entries[index]

    return redirect(f"/wiki/{title}")