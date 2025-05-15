from django.shortcuts import render
from .models import Listing

# Create your views here.
def listings_list(request):
    Listing.objects.all()
    context = {
        "listings": listings
    }
    return render(request, "listings.html", context)