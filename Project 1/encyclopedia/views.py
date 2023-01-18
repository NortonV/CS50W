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