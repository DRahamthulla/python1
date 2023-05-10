from django.urls import path

from . import  views

urlpatterns=[

      path('crea',views.create_session,name='create_session'),
      path('aces',views.access_session,name='access_session'),
      path('del',views.delete_session,name='delete_session'),
]
