from django.urls import path
from . import views

urlpatterns = [

    path('showuser',views.showUser),
    path('showpoem',views.showPoem),
    path('searchuser', views.searchuser),
    path('deluser', views.delUser),

    path('delpoem', views.delPoem),
    path('editpoem', views.editpoem),
    path('searchpoem', views.searchpoem),
    #path('addpoem', views.addPoem),

]

