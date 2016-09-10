from django.contrib import admin

# Register your models here.
from .models import Registrant

def standard_fields(model):
    fields = []
    for field in model._meta.fields:
        if field.get_internal_type() != "ManyToManyField":
            fields.append(field.name)
    return tuple(fields)

class RegistrantAdmin(admin.ModelAdmin):
    list_display = standard_fields(Registrant)
    list_display_links = list_display
admin.site.register(Registrant, RegistrantAdmin)
