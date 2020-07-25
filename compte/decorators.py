from django.http import HttpResponse
from django.shortcuts import redirect

def user_non_authentifier(view_func):
    def myuser(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("home")
        else:
            return view_func(request, *args, **kwargs)
    return myuser


def allowed_users(allowed_roles=[]):
    def decorateur(view_func):
        def fonction_dev(request, *args, **kwargs):

            group = None
            if request.users.exists():
                group = request.users.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse("vous n'est pas autorisé ")
                
        return view_func
    return decorateur

def admin_enligne(view_func):
    def fonction_dev(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'client':
            return redirect("user")

        if group == "admin":
            return view_func(request, *args, **kwargs)

    return fonction_dev
    


            

        
