from django.contrib import admin
from .models import Message

# Register your models here.
class MessageAdmin(admin.ModelAdmin):
    list_display = ['nom','post_nom','email','telephone','message','date']
    list_filter = ['date']
    search_fields = ['nom','post_nom','email']

admin.site.register(Message,MessageAdmin)