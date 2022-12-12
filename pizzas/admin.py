from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Comment)
admin.site.register(Pizza)
admin.site.register(Topping)


class CommentAdmin(admin.ModelAdmin):
    list_display=('name', 'text', 'pizza', 'date_added')
    list_filter=('created_on')
