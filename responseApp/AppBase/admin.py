from django.contrib import admin
from .models import Tovar, Response

# Register your models here.
class BaseAdmin(admin.ModelAdmin):
    save_on_top = True
    list_per_page = 10
    search_fields = ('title',)
    list_filter = ('title', 'date_create')
    class Meta:
        abstract = True

@admin.register(Tovar)
class AdminTovar(BaseAdmin):
    list_display = ('title','date_create','user')
    list_display_links = ('title',)
    fields = ('title','image','description','user')
    readonly_fields = ('date_create',)
    list_filter = ('date_create',)
    
@admin.register(Response)
class AdminResponse(BaseAdmin):
    list_display = ('title','date_create')
    list_display_links = ('title',)
    fields = ('title','text','tovar_rel')
    readonly_fields = ('date_create',)
    list_filter = ('date_create',)