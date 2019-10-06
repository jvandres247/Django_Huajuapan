from django.contrib import admin
from .models import Twit
# Register your models here.

class TwitAdmin(admin.ModelAdmin):
	list_display = ('text', 'thumb_image', 'thumbnail')

admin.site.register(Twit, TwitAdmin)