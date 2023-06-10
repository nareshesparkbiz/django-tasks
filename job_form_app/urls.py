from django.urls import path
from . import views



urlpatterns = [
    path('',views.BasicForm,name='Basic'),
    path('get/<state>',views.get,name='get'),
    path('show-Data/',views.showData,name='showData'),
    path('delete-Data/',views.deleteData,name="deleteData"),

]
