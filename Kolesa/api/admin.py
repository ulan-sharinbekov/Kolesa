from django.contrib import admin
from api.models import *
# Register your models here.
class CityAdmin(admin.ModelAdmin):
    list_display = ('title',)
admin.site.register(City, CityAdmin)

class BrandAdmin(admin.ModelAdmin):
    list_display = ('title',)
admin.site.register(Brand, BrandAdmin)

class ModelsAdmin(admin.ModelAdmin):
    list_display = ('title', 'city', 'year')
admin.site.register(Models, ModelsAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'value', 'car', 'parent')
admin.site.register(Comment, CommentAdmin)
