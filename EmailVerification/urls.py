from django.urls import include,path
from .views import signup,activate

urlpatterns = [  
    
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',  
        activate, name='activate'),  
    path('signup',signup,name='signup'),
]  