from django.shortcuts import render
from django.http import HttpResponse
import markdown2

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def article(request, title):
    markdowner = markdown2.Markdown()
    file = util.get_entry(title.lower())
    if not file:
        file = util.get_entry("404")
    html = markdowner.convert(file)
    return render(request, "encyclopedia/article.html", {
        "file": html,
        "title": html.split("h1")[1][1:-2]
    })

