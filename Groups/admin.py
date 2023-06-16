from django.contrib import admin
from .models import Tags, Squad
# Register your models here.

@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display =("tag_name", "tag_descrip")

@admin.register(Squad)
class SquadAdmin(admin.ModelAdmin):
    list_display =("squad_name", "squad_descrip")