from django.urls import path
from . import views
from django.conf import settings

app_name='paper'
urlpatterns=[
    path('', views.index,name="home"),
    path('folder/<int:id>',views.folder,name="folder"),
    path('search',views.search,name="search"),
    path('bookmark_view',views.bookmark_view,name="bookmark_view"),
    path('bookmark/<int:id>',views.bookmark,name="bookmark"),
    path('bookmark_remove/<int:id>',views.bookmark_remove,name="bookmark_remove")
]