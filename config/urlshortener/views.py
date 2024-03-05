from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect

from .models import Shortener

from .forms import ShortenerForm

# Create your views here.

def home_view(request):
    template = 'urlshortener/home.html'

    context = {}

    context['form'] = ShortenerForm()

    if request.method == 'GET':
        return render(request,template,context)
    
    elif request.method == 'POST':
        used_form = ShortenerForm(request.POST)
        if used_form.is_valid():
            shortened_object = used_form.save()
            new_url = request.build_absolute_uri('/') + shortened_object.short_url

            long_url = shortened_object.long_url

            times = shortened_object.times_followed

            all_urls = Shortener.objects.all()

            context['new_url'] = new_url
            context['long_url'] = long_url
            context['no_of_times'] = times
            context['all_urls'] = all_urls


            return render(request,template,context)
        
    context['errors'] = used_form.errors
    return render(request,template,context)

def redirect_url_view(request, shortened_part):
    try:
        shortener = Shortener.objects.get(short_url=shortened_part)
        shortener.times_followed += 1
        shortener.save()
        return HttpResponseRedirect(shortener.long_url)
    except:
        raise Http404('Sorry this link is broken :()')
    
def view_all_urls(request):
    all_urls = Shortener.objects.all()
    template = 'urlshortener/home.html'
    return render(request,template,{'all_urls':all_urls})