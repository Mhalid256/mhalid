
from django.contrib import admin
from django.urls import path,include
from hk.views import index_view,blog_list_view,add_author_view,edit_author_view,delete_author_view,sign_up_view





urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index_view,name='index_page'), 
    path('','sign_up/',sign_up_view,name='sign_up_page'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('blog_list/' ,blog_list_view, name='blog_list_page'),
    path('add_author/',add_author_view,name="add_author_page"),
    path('edit_author/<int:author_id>/',edit_author_view,name="edit_author_page"),
    path('delete_author/<int:author_id>/',delete_author_view, name="delete_author_page"),
]


