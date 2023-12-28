from django.contrib import admin
from .models import student,reportcard,position

class studentAdmin(admin.ModelAdmin):
    list_display=("std_No","name","gender","std_class","stream","term")
    
class reportcardAdmin(admin.ModelAdmin):
    list_display=("std_No","subject","BOT","MOT","EOT","score","grade","comment","initials","totalmarks","averagemarks")
    
class positionAdmin(admin.ModelAdmin):
    list_display=("std_No","std_class","stream","aggregates","division")
    
# Register your models here.
admin.site.register(student,studentAdmin)
admin.site.register(reportcard,reportcardAdmin)
admin.site.register(position,positionAdmin)