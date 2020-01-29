from django.shortcuts import render
from Blogpost.models import Blogpost



def index(request):
    """View function for home page of site."""
    queryset = Blogpost.objects.order_by('-publish')
    context = {
        'object_list': queryset
    }
    return render(request, 'index.html', context)
