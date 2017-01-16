from django.shortcuts import render
from django.template.context_processors import csrf


def search_post(request):
    ctx = {}
    ctx.update(csrf(request))
    if request.POST:
        ctx['rlt'] = request.POST['q']
    return render(request, "search_post.html", ctx)
