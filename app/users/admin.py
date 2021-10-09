from django.contrib import admin
from users.models import CustomUser, FollowRequest


class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email", "is_staff")
    list_filter = ("date_joined", "is_staff")
    search_fields = ("username", "email",)


admin.site.register(CustomUser, UserAdmin)


class FollowRequestAdmin(admin.ModelAdmin):
    list_display = ("id", "follower", "following", "pending")
    list_filter = ("pending", "request_date")
    search_fields = ("follower__username", "following__username",)


admin.site.register(FollowRequest, FollowRequestAdmin)
