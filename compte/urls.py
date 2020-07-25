from django.urls import path
from . import views


urlpatterns = [

    path("", views.home,name="home"),
    path("produit/", views.produit, name="produit"),
    path("register_client/", views.register_client, name="register_client"),
    path("login_client/", views.login_client, name="login_client"),
    path("logout/", views.logout, name="logout"),
    path("user/", views.user, name="user"),
    path("profile/", views.profile, name="profile"),
    path("client/<str:pk>/", views.client,name="client"),
    path("cree_commande/<str:pk>/", views.cree_commande, name="cree_commande"),
    path("modifier_commande/<str:pk>/", views.modifier_commande, name="modifier_commande"),
    path("supprimer_commande/<str:pk>/", views.supprimer_commande, name="supprimer_commande"),
  
]
