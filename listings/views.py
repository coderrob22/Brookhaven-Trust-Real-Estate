from django.shortcuts import render, get_object_or_404
from .models import Listing
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import state_choices, prices_choices, bedroom_choices


# Create your views here.
def index(request):
    """function for the views of the index."""
    listings = Listing.objects.all().filter(is_published=True)

    # THis is used to setup pagination.
    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }

    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    """function for a single listing to be shown"""
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing':listing
    }

    return render(request, 'listings/listing.html', context)


def search(request):

    context ={
        'state_choices' : state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': prices_choices,
    }
    return render(request, 'listings/search.html', context)