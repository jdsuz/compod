from django.db import models
from users.models import CustomUser

class Feed(models.Model):
    """An RSS feed the user wants to subscribe to."""
    source = models.URLField()
    podcast_name = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.podcast_name

class Episode(models.Model):
    """An episode grabbed from an RSS feed."""
    title = models.CharField(max_length=200)
    description = models.TextField()
    pub_date = models.DateTimeField()
    link = models.URLField()
    image = models.URLField()
    podcast_name = models.CharField(max_length=100)
    guid = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.podcast_name}: {self.title}"
