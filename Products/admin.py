from django.contrib import admin

from .models import *

class categoryAdmin(admin.ModelAdmin):
    list_display=("id","title")
class productAdmin(admin.ModelAdmin):
    list_display=("id","title")



admin.site.register(ProductModel,productAdmin)
admin.site.register(category,categoryAdmin)
admin.site.register(cartModel)