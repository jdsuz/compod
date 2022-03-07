from django.core.management.base import BaseCommand

import feedparser
import ssl
from dateutil import parser

from podcasts.models import Episode

if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context

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

def fetch_killtony_episodes():
    """Fetches new episodes from RSS for the Kill Tony (Tony Hinchcliffe) podcast."""
    _feed = feedparser.parse("https://www.deathsquad.tv/feed/podcast/")
    save_new_episodes(_feed)

def fetch_wemightbedrunk_episodes():
    """Fetches new episodes from RSS for We Might Be Drunk (Mark Normand & Sam Morril) podcast."""
    _feed = feedparser.parse("https://onemoredrinkpod.libsyn.com/rss")
    save_new_episodes(_feed)

def fetch_skeptictank_episodes():
    """Fetches new episodes from RSS for the Skeptic Tank (Ari Shaffir) Podcast."""
    _feed = feedparser.parse("https://feeds.libsyn.com/33779/rss")
    save_new_episodes(_feed)

def fetch_whiskeyginger_episodes():
    """Fetches new episodes from RSS for the Whiskey Ginger (Andrew Santino) Podcast."""
    _feed = feedparser.parse("https://feeds.megaphone.fm/TPC6596839207")
    save_new_episodes(_feed)

def fetch_thispastweekend_episodes():
    """Fetches new episodes from RSS for This Past Weekend (Theo Von) Podcast."""
    _feed = feedparser.parse("https://www.omnycontent.com/d/playlist/9b7dacdf-a925-4f95-84dc-ac46003451ff/d32c6294-eba5-4807-abed-acb8002fdc1c/457951e4-f7cd-44ce-a5ff-acb8002fdc26/podcast.rss")
    save_new_episodes(_feed)

def fetch_timdillon_episodes():
    """Fetches new episodes from RSS for the Tim Dillon Show Podcast."""
    _feed = feedparser.parse("https://feeds.megaphone.fm/TPC2985326322")
    save_new_episodes(_feed)

class Command(BaseCommand):
    def handle(self, *args, **options):
        fetch_killtony_episodes()
        fetch_wemightbedrunk_episodes()
        fetch_thispastweekend_episodes()
        #fetch_skeptictank_episodes()
        #fetch_whiskeyginger_episodes()
        #fetch_timdillon_episodes()
