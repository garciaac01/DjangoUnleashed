from django.shortcuts import redirect

def redirect_root(request):
    """Redirect the user to the blog post list"""
    return redirect('blog_post_list')

