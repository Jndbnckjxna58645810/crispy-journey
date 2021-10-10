from django.contrib import admin
from .models import Bb, Rubric, Salesman

admin.site.register(Rubric)
admin.site.register(Salesman)

class BbAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'published', 'rubric', 'person')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content')

admin.site.register (Bb, BbAdmin)