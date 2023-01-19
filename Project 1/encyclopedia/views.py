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
    if title == "random_article":
        title = random.choice(util.list_entries())
        return redirect(f"/wiki/{title}")
    file = util.get_entry(title.lower())
    if not file:
        file = util.get_entry("404")
    html = markdowner.convert(file)

    return render(request, "encyclopedia/article.html", {
        "file": html,
        "title": html.split("h1")[1][1:-2]
    })

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