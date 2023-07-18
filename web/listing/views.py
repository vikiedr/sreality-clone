from django.shortcuts import render
from django.http import HttpResponse
from .models import Flat

# Create your views here.
def index(request):
    return list_flats(request, None)

def list_flats(request, scrape_id):
    flats = Flat.objects.all().order_by('id')
    unique_scrape_ids = _get_unique_crape_ids(flats.values_list("scrape_id", flat=True))
    scrape_id = scrape_id if scrape_id else unique_scrape_ids[-1]
    selected_flats = flats.filter(scrape_id=scrape_id)
    return render(request, "list_flats.html", {'flats': selected_flats, 'scrape_id': scrape_id, 'scrape_ids': unique_scrape_ids})

def _get_unique_crape_ids(scrape_ids):
    seen = set()
    return [s_id for s_id in scrape_ids if not (s_id in seen or seen.add(s_id))]
