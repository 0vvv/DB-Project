from django.urls import path
from . import views


urlpatterns = [
    path('addcollect', views.addCollect),
    path('checkcollect', views.checkCollect),
    path('delcollect', views.delCollect),

    path('addnote',views.addNote),
    path('checknote', views.checkNote),
    path('delnote',views.delNote),
    path('changenote',views.changeNote),
]