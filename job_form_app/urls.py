from django.urls import path
from . import views



urlpatterns = [
    path('',views.BasicForm,name='Basic'),
    path('get/<state>',views.get,name='get'),
    path('show-Data/',views.showData,name='showData'),
    path('delete-Data/',views.deleteData,name="deleteData"),
    path('search/',views.searchData,name='searchData'),
    path('form/edit/<int:id>/', views.edit_form, name='form-edit'),

]
