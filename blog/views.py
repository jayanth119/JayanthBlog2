

from blog.models import Post, Category 
from django.shortcuts import render, get_object_or_404


# from django.http import HttpResponseRedirect
# from django.urls import reverse
# def  get_client_id(request):
#     x = request.META.get('HTTP_X_FORWARDED_FOR')
#     if x :
#         ip =  x.split(',')[0]
#     else :
#         ip = request.META.get('REMOTE_ADDR')
#     return ip 
        
# def postlike(request , pk):
#     post_id =request.POST.get('post_id')
#     post = Post.objects.get(pk = post_id)
#     ip = get_client_id(request)
#     if not Ipmodel.objects.filter(ip = ip).exists():
#         Ipmodel.objects.create(ip)
#     if Post.likes.filter(id = Ipmodel.objects.get(ip).id).exists():
#         Post.likes.remove(Ipmodel.objects.get(ip  = ip ))
#     else :
#         Post.likes.add(Ipmodel.objects.get(ip  = ip ))
#     return HttpResponseRedirect(reverse('post_detail', args = [post_id]))
        
     

# Create your views here.
def home(request):
    # load all the post from db(10)
    posts = Post.objects.all()[:11]
    # print(posts)

    cats = Category.objects.all()

    data = {
        'posts': posts,
        'cats': cats
    }
    return render(request, 'home.html', data)
def main(request):
    return render(request , 'main.html')


def post(request, url):
    post = get_object_or_404(Post, url=url)
    cats = Category.objects.all()

    return render(request, 'posts.html', {'post': post, 'cats': cats})
def about(request):
    return render(request , 'about.html')

def category(request, url):
    cat = Category.objects.get(url=url)
    posts = Post.objects.filter(cat=cat)
    return render(request, "category.html", {'cat': cat, 'posts': posts})
