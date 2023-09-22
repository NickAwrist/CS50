import random
import markdown

from django.shortcuts import redirect
from django.shortcuts import render
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })



def search(request):
    entry_name = request.GET.get("entryName")
    entries = util.list_entries()

    entry_name = entry_name.lower()

    if entry_name in [entry.lower() for entry in entries]:
        return redirect('entry', entry=entry_name)

    return relatedEntries(request)


def toPage(request, entry):
    entry_content = util.get_entry(entry)

    if entry_content:
        html_content = markdown.markdown(entry_content)

        return render(request, "encyclopedia/entry.html", {
            "entryName": entry,
            "markdown_content": html_content
        })
    else:
        return render(request, "encyclopedia/pageNotFound.html")


def editPage(request, entry):
    entry_content = util.get_entry(entry)

    if entry_content:
        html_content = markdown.markdown(entry_content)

        return render(request, "encyclopedia/editEntry.html", {
            "entryName": entry,
            "markdown_content": html_content
        })
    else:
        return render(request, "encyclopedia/pageNotFound.html")


def saveEntry(request, entry):
    markdown_text = request.POST.get('markdown_text', '')

    util.save_entry(entry, markdown_text)

    return redirect('entry', entry=entry)


def addEntryPage(request):
    return render(request, "encyclopedia/addEntry.html")


def addEntrySubmit(request):
    title = request.POST.get('entryName')
    markdown_text = request.POST.get('markdown_text')

    entry_name = title.lower()
    entries = util.list_entries()
    
    if entry_name in [entry.lower() for entry in entries]:
        return render(request, "encyclopedia/addEntry.html", {
            "entry_exists": True,
            "entryName":entry_name,
            "markdown_text":markdown_text
        })

    util.save_entry(title, markdown_text)

    return redirect('entry', entry=title)


def randomPage(request):
    entry_list = util.list_entries()

    if entry_list:
        random_entry = random.choice(entry_list)
        return redirect('entry', entry=random_entry)
    else:
        return render(request, "encyclopedia/index.html", {
            "entries": util.list_entries()
        })

def containsSubString(string1, string2):
    return string2.lower() in string1.lower()


def relatedEntries(request):
    entry_name = request.GET.get("entryName")
    entries = util.list_entries()

    updatedEntries = []

    for entry in entries:
        if containsSubString(entry.lower(), entry_name.lower()):
            updatedEntries.append(entry)

    return render(request, "encyclopedia/similarSearches.html", {
        "entries": updatedEntries,
        "result": entry_name
    })
    
