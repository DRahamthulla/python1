from django.urls import path
from django.views.decorators.cache import cache_page

from . import  views
from .views import  showcookie,delete_co,setcookie

urlpatterns = [
    path('set',views.setcookie,name='setcookie'),
    path('show',views.showcookie,name='showcookie'),
    path('del',views.delete_co,name='delete_c0'),
    path('index', cache_page(200)(views.index))

]