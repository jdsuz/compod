from django.contrib import admin

from .models import Episode, Feed

@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    list_display = ("podcast_name", "title", "pub_date")

@admin.register(Feed)
class FeedAdmin(admin.ModelAdmin):
    list_display = ("podcast_name", "source", "date_added")