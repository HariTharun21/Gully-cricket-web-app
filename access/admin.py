from django.contrib import admin

# Register your models here.
# access/admin.py
from django.contrib import admin
from .models import AccessPermission, AccessRequest

# ----------------------------
# Admin for AccessPermission
# ----------------------------
class AccessPermissionAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'main_user',
        'access_type',
        'match',
        'player',
        'team',
        'active',
        'granted_at'
    )
    list_filter = ('access_type', 'active', 'granted_at')
    search_fields = ('user__username', 'main_user__username')

# ----------------------------
# Admin for AccessRequest
# ----------------------------
class AccessRequestAdmin(admin.ModelAdmin):
    list_display = (
        'requester',
        'status',
        'match',
        'player',
        'team',
        'requested_at'
    )
    list_filter = ('status', 'requested_at')
    search_fields = ('requester__username',)

# Register models
admin.site.register(AccessPermission, AccessPermissionAdmin)
admin.site.register(AccessRequest, AccessRequestAdmin)
