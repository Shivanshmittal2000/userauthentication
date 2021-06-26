from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('show/<int:id>/',views.show,name='show'),
    path('show/<int:id>',views.deletedata,name='deletedata'),
    path('showuser/<int:id>',views.useredit,name='userediting'),
    path('showemail/<int:id>',views.emailedit,name='emailediting'),
    path('showaddress/<int:id>',views.addressedit,name='addressediting')
]
