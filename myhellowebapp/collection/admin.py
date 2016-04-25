from django.contrib import admin

# importing the model
from collection.models import Thing

#setup automated slug creation
class ThingAdmin(admin.ModelAdmin):
    model = Thing
    list_display = ('name', 'description',)
    prepopulated_fields = {'slug': ('name',)}

# and then register it
admin.site.register(Thing, ThingAdmin)