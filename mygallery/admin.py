from django.contrib import admin
from .models import Uploader, Pdetails, tags

class PdetailsAdmin(admin.ModelAdmin):
    filter_horizontal =('tags',)
# Register your models here.
admin.site.register(Uploader)
admin.site.register(Pdetails,PdetailsAdmin)
admin.site.register(tags)
