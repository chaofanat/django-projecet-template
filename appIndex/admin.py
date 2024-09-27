from django.contrib import admin
from django.utils.translation import gettext_lazy as _

# Register your models here.


from appIndex.models import application
class applicationAdmin(admin.ModelAdmin):
    list_display = ('name','url','description','icon','is_active','create_time','update_time')
    list_filter = ('name','url','description','icon','is_active','create_time','update_time')
    search_fields = ('name','url','description','icon','is_active')
    ordering = ('-create_time',)
    fieldsets = (
        (None, {
            'fields': ('name','url','description','icon','is_active')
        }),
    )
    actions = ['make_active','make_inactive']
    def make_active(self, request, queryset):
        queryset.update(is_active=True)
    make_active.short_description = _("Mark selected applications as active")
    def make_inactive(self, request, queryset):
        queryset.update(is_active=False)
    
    make_inactive.short_description = _("Mark selected applications as inactive")

admin.site.register(application, applicationAdmin)