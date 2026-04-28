from django.contrib import admin
from apps.products.models import Jam, ImgJam, Category


class ImgJamInline(admin.TabularInline):
    model = ImgJam
    extra = 1


@admin.register(Jam)
class JamAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc')
    inlines = [ImgJamInline,]
    prepopulated_fields = {'slug':('title',)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',) 
    prepopulated_fields = {'slug':('name',)}