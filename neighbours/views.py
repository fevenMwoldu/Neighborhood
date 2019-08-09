from django.shortcuts import render
from django.http  import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from . models import Neighbourhood,NeighbourhoodUser,Bussiness,Profile,Postcontent,NeighbourhoodLetterRecipients
from .email import send_welcome_email
from .forms import NeighbourhoodForm

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    current_user = request.user 
    form = NeighbourhoodForm(request.POST)
    if request.method == 'POST':
        # form = NeighbourhoodForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']

            recipient = NeighbourhoodLetterRecipients(name = name,email =email)
            recipient.save()
            send_welcome_email(name,email)
            HttpResponseRedirect('index')

    contents = Postcontent.objects.all()
    bussinesses = Bussiness.objects.all()
    return render(request, 'index.html',{"contents" : contents,"bussinesses" : bussinesses,"letterForm":form})


def search_results(request):

    if 'search_term' in request.GET and request.GET["search_term"]:
        search_term = request.GET.get("search_term")
        searched_bussinesses = Bussiness.search_by_bussinessname(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"bussinesses": searched_bussinesses})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

    
   
