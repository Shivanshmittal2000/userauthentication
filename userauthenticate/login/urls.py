from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('show/<int:id>/',views.show,name='show')
]
