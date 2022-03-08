from django.views.generic import ListView
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Episode, Feed
from .forms import FeedForm

import feedparser
import ssl
from dateutil import parser

if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context

class HomePageView(ListView):
    template_name = "homepage.html"
    model = Episode

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["episodes"] = Episode.objects.filter().order_by("-pub_date")[:25]
        return context

def save_new_episodes(feed):
    """Saves new episodes to the database.
    Checks the episode GUID against the episodes currently stored in the
    database. If not found, then a new `Episode` is added to the database.

    Args:
        feed: requires a feedparser object
    """
    podcast_title = feed.channel.title
    podcast_image = feed.channel.image["href"]

    for item in feed.entries:
        if not Episode.objects.filter(guid=item.guid).exists():
            episode = Episode(
                title=item.title,
                description=item.description,
                pub_date=parser.parse(item.published),
                link=item.link,
                image=podcast_image,
                podcast_name=podcast_title,
                guid=item.guid,
            )
            episode.save()

@login_required
def fetch_episodes(request):
    """Display a user's personalized podcast feed."""
    feeds = Feed.objects.filter(owner=request.user)
    for feed in feeds:
        _feed = feedparser.parse(feed)
        save_new_episodes(_feed)


@login_required
def new_feed(request):
    """Add a new feed."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = FeedForm()
    else:
        # POST data submitted; process data.
        form = FeedForm(request.POST)
        if form.is_valid():
            new_feed = form.save(commit=False)
            new_feed.owner = request.user
            form.save()
            return HttpResponseRedirect(reverse('home'))

    context = {'form': form}
    return render(request, 'new_feed.html', context)
