from django.shortcuts import render
from django.http import HttpResponseRedirect

import requests
from bs4 import BeautifulSoup

from myapp.models import Link

# Create your views here.
def scrape(request):

    if request.method == 'POST':
        site = request.POST.get('site')

        page = requests.get(site)
        soup = BeautifulSoup(page.text, 'html.parser')

        for link in soup.find_all('a'):
            link_text = link.string
            link_address = link.get('href')

            Link.objects.create(
                name=link_text,
                address=link_address,
            )

        return HttpResponseRedirect('/')

    else:
        data = Link.objects.all()

    return render(request, 'myapp/result.html', {'data': data})


def clear(request):

    Link.objects.all().delete()
    return render(request, 'myapp/result.html')
