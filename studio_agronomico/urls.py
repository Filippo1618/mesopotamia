from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('chi_siamo/', views.chi_siamo, name="chi_siamo"),
    path('consulenze/', views.consulenze, name="consulenze"),
    path('contatti/', views.contatti, name="contatti"),
    path('servizi/', views.servizi, name="servizi"),
    path('news/', views.news, name="news"),
    path('blogpost_detail/<int:id>', views.blogpost_detail, name="blogpost_detail"),
    path('blogpost_detail/<int:id>/follow/', views.follow_blogpost, name="follow_blogpost"),
    path('blogpost_detail/<int:id>/unfollow/', views.unfollow_blogpost, name="unfollow_blogpost"),
    path('registrazione/', views.registrazione, name="registrazione"),
    path('registrazione/createUser/', views.createUser, name="createUser"),
    path('login/', views.login_page, name="login"),
    path('login/login_req/', views.login_req, name="login_req"),
    path('logout/', views.logout_page, name="logout"),
    path('profilo/', views.profilo, name="profilo"),
    path('servizi_agricoltura/', views.servizi_agricoltura, name="servizi_agricoltura"),
    path('servizi_ambiente/', views.servizi_ambiente, name="servizi_ambiente"),
    path('servizi_verde/', views.servizi_verde, name="servizi_verde"),
    path('servizi_attivita/', views.servizi_attivita, name="servizi_attivita"),
    path('servizi_certificazione/', views.servizi_certificazione, name="servizi_certificazione"),
    path('servizi_economici/', views.servizi_economici, name="servizi_economici"),
]