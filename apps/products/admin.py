from django.contrib import admin
from apps.products.models import Jam, ImgJam


class ImgJamInline(admin.TabularInline):
    model = ImgJam
    extra = 1


@admin.register(Jam)
class JamAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc')
    inlines = [ImgJamInline,]


