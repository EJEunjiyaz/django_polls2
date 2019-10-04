from django.contrib import admin

from .models import Item, Choice

admin.site.site_header = 'Fuck you'
admin.site.site_title = 'my_mind_smile'
admin.site.index_title = 'I love you'

class ChoiceInline(admin.TabularInline):
    model = Choice

class ItemAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

admin.site.register(Item, ItemAdmin)