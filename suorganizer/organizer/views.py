# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http.response import Http404, HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render_to_response, render
from .models import Tag, Startup

# Create your views here.
def tag_list(request):
    # Old code -- no shortcuts
    # tag_list = Tag.objects.all()
    # template = loader.get_template(
    #     'organizer/tag_list.html'
    # )
    # context = {'tag_list':tag_list}
    # output = template.render(context)
    # return HttpResponse(output)

    # Using render_to_response shortcut
    #return render_to_response('organizer/tag_list.html', {'tag_list':Tag.objects.all()})
    #Best way: Use render, which uses a RequestContext object instead of Context
    return render(request, 'organizer/tag_list.html', {'tag_list':Tag.objects.all()})

def tag_detail(request, slug):
    # Lines 27-30 are replaced with 31-33--shortcut for 
    # getting object or raising 404 error
    # try:
    #     tag = Tag.objects.get(slug__iexact = slug)
    # except Tag.DoesNotExist:
    #     raise Http404
    tag = get_object_or_404(
        Tag, slug__iexact=slug
    )

    return render(request, 'organizer/tag_detail.html', {"tag": tag})

def startup_list(request):
    return render(
        request,
        'organizer/startup_list.html', 
        {'startup_list':Startup.objects.all()})

def startup_detail(request, slug):
    startup = get_object_or_404(
        Startup, slug__iexact=slug
    )
    return render(request, 'organizer/startup_detail.html', {'startup':startup})
