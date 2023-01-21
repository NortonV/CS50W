from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import RedirectView

import markdown2
from . import util
import random


markdowner = markdown2.Markdown()

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def article(request, title):
    if request.method == "GET":
        file = util.get_entry(title.lower())
        if not file:
            return render(request, "encyclopedia/error.html", {
            "message": "Entry not found."
            })
        html = markdowner.convert(file)

        return render(request, "encyclopedia/article.html", {
            "file": html,
            "title": html.split("h1")[1][1:-2],
        })
    else:
        content = request.POST.get("content")
        content = f"# {title.capitalize() if not title.isupper() else title}" + "\n" + f"[Edit](/edit/{title.lower()}) " + "\n\n" + content
        util.save_entry(title.lower(), content)
        return redirect(f"/wiki/{title.lower()}")

def random_article(request):
    title = random.choice(util.list_entries())
    return redirect(f"/wiki/{title}")

def search(request):
    query = request.GET.get('q')
    all = util.list_entries()
    if query in all:
        return redirect(f"/wiki/{query.lower()}")
    else:
        results = []
        for i in all:
            if query in i:
                results.append(i)
        return render(request, "encyclopedia/search.html", {
        "results": results,
        "query": query
    })

def new(request):
    if request.method == "GET":
        return render(request, "encyclopedia/new.html")
    else:
        title = request.POST.get("title").strip()
        content = request.POST.get("content")
        if title.lower() in util.list_entries():
            return render(request, "encyclopedia/error.html", {
                "message": f"The entry {title.lower()} already exists."
            })
        else:
            content = f"# {title.capitalize() if not title.isupper() else title}" + "\n" + f"[Edit](/edit/{title.lower()}) " + "\n\n" + content
            util.save_entry(title.lower(), content)
            return redirect(f"/wiki/{title.lower()}")

def edit(request, title):
    file = util.get_entry(title)
    html = markdowner.convert(file)
    return render(request, "encyclopedia/edit.html", {
        "file": "\n".join(file.split("\n")[3:]),
        "title": html.split("h1")[1][1:-2],
    })