from django.contrib import admin

from .models import *
class KinofilmAdmin(admin.ModelAdmin):
    list_display = ('id','Name','photo','Description','Price','Place')
    list_display_links = ('id','Name')
    search_fields = ('title','content')

# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name')
#     list_display_links = ('id','name')
#     search_fields = ('name')

admin.site.register(Users)
admin.site.register(Movie,KinofilmAdmin)
#admin.site.register(Category,CategoryAdmin)