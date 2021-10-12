from django.contrib import admin
from ideas.models import Idea

class IdeaAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "visibility", "date_created")
    list_filter = ("visibility", "date_created")
    search_fields = ("user__username", "visibility",)

admin.site.register(Idea, IdeaAdmin)