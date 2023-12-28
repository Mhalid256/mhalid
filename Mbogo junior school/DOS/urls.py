from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
     path('admin:index/', admin.site.urls),
    path('',views.index,name='index'),
    path('<int:id>',views.view_student,name='view_student'),
    path('add/',views.add,name='add'),
    path('edit/<int:id>/',views.edit,name='edit'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('',views.theme,name='theme'),
    path('pdf',views.pdf,name='pdf'),
    path('excel',views.generate_report_card,name='excel'),
]
