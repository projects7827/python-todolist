from django.urls import path
from .views import delete,index,add

urlpatterns = [ 
    path("",index,name ="home"),
    path("delete",delete,name ="delete"),
    path("add",add,name ="add")
]
    
    
