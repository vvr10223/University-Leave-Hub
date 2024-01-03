from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('register/',register,name='register'),
    path('login/',login,name='login'),
    path('logout/',logout,name='logout'),
    path('',include('leaves.urls')),
    path('',include('leaves.urls')),
    path('',include('leaves.urls')),
]
