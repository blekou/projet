from django.shortcuts import render,redirect
from django.forms import inlineformset_factory
from .models import Produit,Commande,Client 
from django.contrib.auth.models import Group
from .forms  import CommandeForm,MyUserForm,ClientForm
from .filters import CommandeFilter
from django.contrib.auth.forms import UserCreationForm 
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .decorators import user_non_authentifier, allowed_users, admin_enligne


@login_required(login_url = 'login')
@admin_enligne
def home(request):

    commande         = Commande.objects.all()
    client           = Client.objects.all()
    total_client     = client.count()
    total_commande   = commande.count()
    attente          = commande.filter(status='en attente').count()
    livrer           = commande.filter(status='livrer').count()

    datas = {
        'commande':commande,
        'client':client,
        'attente':attente,
        'total_commande':total_commande,
        'livrer': livrer,
        'total_client':total_client,
    }
    return render(request,'compte/dashboard.html',datas)


@login_required(login_url = 'login')
@allowed_users(allowed_roles=["admin"])
def produit(request):
    produit = Produit.objects.all()
    
    datas ={
        'produit':produit,
        
    }
    return render(request,'compte/produit.html',datas)


@login_required(login_url = 'login')
@allowed_users(allowed_roles=["admin"])
def client(request, pk):
    client = Client.objects.get(id=pk)
    commandes = client.commande_set.all()
    total_commande = commandes.count()
    myfilter = CommandeFilter(request.GET, queryset=commandes)

    commandes = myfilter.qs

    datas = {
        'client':client,
        'commandes':commandes,
        'total_commande':total_commande,
        'myfilter':myfilter,
    }
    return render(request,'compte/client.html',datas)


@login_required(login_url = 'login')
@allowed_users(allowed_roles=["admin"])
def cree_commande(request, pk):
    CommandeFormSet = inlineformset_factory(Client, Commande, fields =('client','produit','status','prix','nombre_produit'),extra=5)
    client = Client.objects.get(id = pk)
    formset = CommandeFormSet(instance=client)
    
    if request.method == 'POST':
        formset = CommandeFormSet(request.POST, instance=client)
        if formset.is_valid():
            formset.save()
            prix = formset.cleaned_data.get('prix')
            return redirect("/")
    
    datas = {
        'formset':formset,
    }
    return render(request,'compte/cree_commande.html',datas)


@login_required(login_url = 'login')
@allowed_users(allowed_roles=["admin"])
def modifier_commande(request,pk):

    modifier = Commande.objects.get(id=pk)
    form = CommandeForm(instance = modifier)

    if request.method == 'POST':
        form = CommandeForm(request.POST, instance=modifier)
        if form.is_valid():
            form.save()
            return redirect("/")

    datas = {
        'form':form,
        'modifier':modifier,
    }
    return render(request,'compte/cree_commande.html',datas)


@login_required(login_url = 'login')
@allowed_users(allowed_roles=["admin"])
def supprimer_commande(request,pk):
    
    supprimer = Commande.objects.get(id=pk)
    if request.method == 'POST':
        supprimer.delete()
        return redirect('/')
            
    datas = {
        'item':supprimer,
    }
    return render(request,'compte/supprimer_commande.html',datas)



@allowed_users(allowed_roles=["admin"])
def register_client(request):

    form = MyUserForm()

    if request.method =="POST":
        form = MyUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            messages.success(request,'félicitation votre compte à bien été crée '+ username)


            return redirect('login_client')
    

    datas = {
        "form":form,
    }
    return render(request,'compte/register.html',datas)

@allowed_users(allowed_roles=["admin"])
def login_client(request):
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            messages.info(request, "mot de passe ou pseudo incorrect !")   

    datas = {

    }
    return render(request,'compte/login.html',datas)


def logout(request):
    datas = {
       
    }
    return render(request, 'compte/login.html', datas)


@login_required(login_url = 'login')
@allowed_users(allowed_roles=["client"])
def user(request):

    commandes        = request.user.client.commande_set.all()
    total_commande   = commandes.count()
    attente          = commandes.filter(status='en attente').count()
    livrer           = commandes.filter(status='livrer').count()

    datas = {
        'total_commande':total_commande,
        'livrer': livrer,
        'attente':attente,
        'commandes':commandes,
        
    }
    return render(request, 'compte/user.html', datas)


@login_required(login_url = 'login')
@allowed_users(allowed_roles=["client"])
def profile(request):
    client = request.user.client
    form = ClientForm(instance=client)

    if request.method == "POST":
        form = ClientForm(request.POST, request.FILES, instance=client)
        if form.is_valid():
            form.save()
                
    datas = {
        
        'form':form,
    }
    return render(request, 'compte/profile.html', datas)