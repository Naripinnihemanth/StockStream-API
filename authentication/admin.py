from django.contrib import admin
from .models import *

class addressAdmin(admin.ModelAdmin):
    list_display=("auther","city","default")
admin.site.register(custemUserModel)
admin.site.register(historyModel)
admin.site.register(addreddModel,addressAdmin)
admin.site.register(UserOrdersModel)
# admin.site.register(AllOrderedProducts)