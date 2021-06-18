from django.urls import path
from django.conf.urls import url
from.views import *

urlpatterns = [
    path('',index),
    
     path('about/',index),
    path('live',index),
    path('score/<int:room>/',index),
    path('results/<str:team>/',index),
    
   
    
]