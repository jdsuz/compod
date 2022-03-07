from django.views.generic import ListView
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Episode, Feed
from .forms import FeedForm

class HomePageView(ListView):
    template_name = "homepage.html"
    model = Episode

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["episodes"] = Episode.objects.filter().order_by("-pub_date")[:25]
        return context

def new_feed(request):
    """Add a new feed."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = FeedForm()
    else:
        # POST data submitted; process data.
        form = FeedForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('podcasts:home'))

    context = {'form': form}
    return render(request, 'new_feed.html', context)
