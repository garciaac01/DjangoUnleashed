# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render_to_response, render
from django.views.generic import View

from .models import Post

# Create your views here.
class PostList(View):
    template_name = 'blog/post_list.html'
    def get(self, request, parent_template=None):
        return render(request, self.template_name, 
                    {'post_list':Post.objects.all()})

def post_detail(request, year, month, slug, parent_template=None):
    post = get_object_or_404(
        Post,
        pub_date__year=year,
        pub_date__month=month,
        slug=slug
    )
    return render(request, 'blog/post_detail.html', {'post':post})