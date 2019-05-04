from django.contrib import admin
from .models import contactos
# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

admin.site.register(contactos,ProjectAdmin)