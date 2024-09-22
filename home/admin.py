from django.contrib import admin
from .models import Category, Dish, Gallery, Contact, Staff, Event
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'is_visible', 'created_at', 'updated_at')
    list_filter = ('is_visible','created_at', 'updated_at')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    date_hierarchy = ('created_at')

admin.site.register(Dish)
admin.site.register(Gallery)
admin.site.register(Contact)
admin.site.register(Staff)
admin.site.register(Event)

