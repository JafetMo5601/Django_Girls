from django.shortcuts import render

def post_list(request):
    return render(request, 'Blogs/post_list.html', {})