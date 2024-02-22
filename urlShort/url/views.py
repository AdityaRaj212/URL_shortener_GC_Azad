from django.shortcuts import render,redirect
import random
import string
from django.http import HttpResponse
from .models import UrlData
from django import forms

# Create your views here.
class Url(forms.Form):
    url = forms.CharField(label="URL")

def index(request):
    return HttpResponse("Hello World")

def urlShort(request):
    if request.method == 'POST':
        form = Url(request.POST)
        if form.is_valid():
            slug = ''.join(random.choice(string.ascii_letters) for x in range(10))
            url = form.cleaned_data["url"]
            new_url = UrlData(url=url,slug=slug)
            new_url.save()
            request.user.urlshort.add(new_url)
            return redirect('/')
        else:
            form = Url()
        data = UrlData.objects.all()
        context = {
            'form': form,
            'data': data
        }
        return render(request,'index.html',context)
    
def urlRedirect(request,slugs):
    data = UrlData.objects.get(slug=slugs)
    return redirect(data.url)



