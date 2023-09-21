from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import BlogPost
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from . decorators import login_required_for_registration

# Create your views here.

def index(request):
    template = loader.get_template('studio_agronomico/index.html')
    return HttpResponse( template.render({}, request))

def chi_siamo(request):
    template = loader.get_template('studio_agronomico/chi_siamo.html')
    return HttpResponse( template.render())

def consulenze(request):
    template = loader.get_template('studio_agronomico/consulenze.html')
    return HttpResponse( template.render())

def contatti(request):
    template = loader.get_template('studio_agronomico/contatti.html')
    return HttpResponse( template.render())

def servizi(request):
    template = loader.get_template('studio_agronomico/servizi.html')
    return HttpResponse( template.render())


def news(request):
    posts = BlogPost.objects.filter(new=False)
    newPosts = BlogPost.objects.filter(new=True)

    template = loader.get_template('studio_agronomico/news.html')
    context = {
        'posts' : posts,
        'newPosts' : newPosts
    }
    return HttpResponse( template.render(context, request))


def blogpost_detail(request, id):
    blogpost = get_object_or_404(BlogPost, id=id)

    return render(request, 'studio_agronomico/blogpost_detail.html', {'blogpost': blogpost})


# una wrapped view per impedire a chi ha fatto il log in di registrarsi senza prima fare logout
def login_required_for_registration(view_func):
    def _wrapped_view(request, *args, **kwargs):
        # Verifica se l'utente è autenticato
        if request.user.is_authenticated:
            messages.error(request,"Devi fare il log out prima di procedere con la registrazione di un account")
            # Utente già autenticato, reindirizza a una pagina specifica (ad esempio il profilo)
            return redirect('profilo')  # Cambia questo percorso in base alla tua configurazione
        else:
            # Utente non autenticato, permetti l'accesso alla pagina di registrazione
            return view_func(request, *args, **kwargs)
    return _wrapped_view


def createUser(request):
    
    template = loader.get_template('studio_agronomico/index.html')

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        nome = request.POST['nome']
        cognome = request.POST['cognome']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if User.objects.filter(username=username):
            messages.error(request, 'Username already exists')
            return HttpResponseRedirect(reverse('login'))
        
        if User.objects.filter(email=email):
            messages.error(request, 'Username already exists')
            return HttpResponseRedirect(reverse('login'))

        if len(username) > 10:
            messages.error(request, "Username too long")
            return HttpResponseRedirect(reverse('login'))
        
        if password1 != password2:
            messages.error(request, "Le password non coincidono")
            return HttpResponseRedirect(reverse('login'))
        
        if not username.isalnum():
            messages.error(request, "l' username deve essere alfanumerico")
            return HttpResponseRedirect(reverse('login'))
                                        
        new_user = User.objects.create_user(username=username, password=password1)
        new_user.first_name = nome
        new_user.email = email
        new_user.last_name = cognome

        new_user.save()

        messages.success(request,"Il tuo account è stato creato correttamente!")
    # return redirect('studio_agronomico/index.html')
    return HttpResponse( template.render({}, request))

@login_required_for_registration
def registrazione(request):
    
    template = loader.get_template('studio_agronomico/registrazione.html')
    return HttpResponse( template.render({},request))


def login_req(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        print(username,password)
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)

            template = loader.get_template('studio_agronomico/login.html')

            context = {
                "user": user
            }

            return HttpResponse( template.render(context ,request))
        else:
            messages.error(request,"username o passsword errati")
            return HttpResponseRedirect(reverse('login'))
    return HttpResponseRedirect(reverse('login'))


def login_page(request):

    template = loader.get_template('studio_agronomico/login.html')
    return HttpResponse( template.render({},request))



def logout_page(request):

    logout(request)
    messages.error(request,"logout effettuato correttamente")
    return HttpResponseRedirect(reverse('login'))


@login_required
def profilo(request):

    template = loader.get_template('studio_agronomico/profilo.html')

    # Ottieni l'oggetto UserProfile associato all'utente
    user = request.user
    followed_blogposts = user.userprofile.followed_blogposts.all()
    template = loader.get_template('studio_agronomico/profilo.html')

    context = {
        'user': user,  # Passa l'oggetto User al template
        'followed_blogposts' : followed_blogposts, # Passa la lista di blogposts seguiti
    }

    return HttpResponse( template.render(context ,request))

@login_required
def follow_blogpost(request, id):
    blogpost = get_object_or_404(BlogPost, id=id)

    if request.user in blogpost.followers.all():
        messages.info(request, 'Hai già iniziato a seguire questo blogpost.')
    else:
        blogpost.followers.add(request.user)
        request.user.userprofile.followed_blogposts.add(blogpost)
        messages.success(request, 'Hai iniziato a seguire questo blogpost.')

    return redirect('blogpost_detail', id=id)

@login_required
def unfollow_blogpost(request, id):
    blogpost = get_object_or_404(BlogPost, id=id)

    if request.user in blogpost.followers.all():
        blogpost.followers.remove(request.user)
        request.user.userprofile.followed_blogposts.remove(blogpost)
        messages.success(request, 'Hai smesso di seguire questo blogpost.')
    else:
        messages.info(request, 'Non stai seguendo questo blogpost.')

    return redirect('blogpost_detail', id=id)
