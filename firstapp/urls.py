from django.urls import path
from firstapp import views

urlpatterns = [ 
    path("",views.index,name ="home"),
    path("/delete",views.delete_record,name ="delete")
]
    
    
