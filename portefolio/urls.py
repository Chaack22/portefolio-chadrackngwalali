from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('envoyer/message/',views.send_messagepage, name='send_message'),
    path('message/',views.messagepage, name='message'),
    path('connexion/',views.loginpage, name='login'),
    path('deconnexion/',views.logoutpage, name='logout'),
]
