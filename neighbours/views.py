from django.shortcuts import render
from django.http  import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from . models import Neighbourhood, CustomUser, Bussiness, Post
from .email import send_welcome_email
from .forms import NeighbourhoodForm,CustomUserForm,PostForm,BussinessForm

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    current_user = request.user 

    custom_user = CustomUser.objects.filter(user_id=current_user.id).first()

    if custom_user is None:
        return HttpResponseRedirect('profile')

    posts = Post.objects.filter(neighbourhood_id=custom_user.neighbourhood.id)

    is_admin = True if current_user == custom_user.neighbourhood.admin else False
    
    return render(request, 'index.html', {"posts": posts, "neighbourhood": custom_user.neighbourhood.name, "is_admin": is_admin})

@login_required(login_url='/accounts/login/')
def add_profile(request):
    current_user = request.user

    if request.method == 'POST':
        form = CustomUserForm(request.POST, request.FILES)
        if form.is_valid():
            custom_user = form.save(commit=False)
            custom_user.user = current_user
            custom_user.save()

            send_welcome_email(custom_user.fullname(), current_user.email)

            return HttpResponseRedirect('/')

    else:
        form = CustomUserForm()

    return render(request, 'add_profile.html', {"form": form})


@login_required(login_url='/account/login/')
def add_post(request):
    print('add_post is called ....')
    current_user = request.user
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            
            custom_user = CustomUser.objects.filter(user_id=current_user.id).first()
            post.created_by = custom_user
            post.neighbourhood = custom_user.neighbourhood

            post.save()
            print('Saved post {}'.format(post))

            return HttpResponseRedirect('/')

    return render(request, 'add_post.html', {"form": form})


@login_required(login_url='/accounts/login/')
def add_bussiness(request):
    current_user = request.user

    if request.method == 'POST':
        form = BussinessForm(request.POST, request.FILES)
        if form.is_valid():
            custom_user = form.save(commit=False)
            custom_user.user = current_user
            custom_user.save()

            

            return HttpResponseRedirect('/')

    else:
        form = BussinessForm()

    return render(request, 'add_bussiness.html', {"form": form})


def search_results(request):

    if 'search_term' in request.GET and request.GET["search_term"]:
        search_term = request.GET.get("search_term")
        searched_bussinesses = Bussiness.search_by_bussinessname(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"bussinesses": searched_bussinesses})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

    
   
