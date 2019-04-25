from django.urls import path
from django.contrib import admin

from application import views

urlpatterns = [
    path('signup/', views.show_signup),
    path('admin/', admin.site.urls),
]