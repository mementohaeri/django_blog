from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone

from .models import Post

def post_list_response(request):
    name = 'Django'
    response = HttpResponse(f'<h1> Hello {name}!!</h1>', content_type="text/html")
    response.write(f'<h1> Hello {name}!!</h1>')
    response.write(f'<p>HTTP Method : {request.method}</p>')
    response.write(f'<p>HTTP ContentType : {request.content_type}</p>')
    #return HttpResponse(f'''<h1> Hello {name}!!</h1><p>HTTP METHOD : {request.method}</p>''')
    return response

# post 목록
def post_list(request):
    posts = Post.objects.filter(posted_date__lte = timezone.now()).order_by('posted_date')
    return render(request, 'product/post_list.html', {'posts': posts})

# Post 상세 목록
def post_detail(request, pk):
    # pk(왼)은 get_object_or_404()에 있는 param
    post = get_object_or_404(Post, pk=pk)
    return render(request,'product/post_detail.html', {'post': post})
