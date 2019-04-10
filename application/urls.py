from django.urls import path

from application import views

urlpatterns = [
    path('signup/', views.show_signup)
]