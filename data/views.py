import json
from pydoc import describe
from django.shortcuts import render, HttpResponse
import requests
from .models import ItunesApple

# Create your views here.


def Index(request):
    if request.method == 'POST':
        itune_id = request.POST.get('itune_id', '')  #284910350
        if itune_id == '':
            x = requests.get('https://itunes.apple.com/lookup?id=284910350')
        else:
            x = requests.get(f'https://itunes.apple.com/lookup?id={itune_id}')
        itunes_data = json.loads(x.text)
        print(itunes_data)
        if itunes_data['results']:
            desc = itunes_data['results'][0]['description']
            genres = str(itunes_data['results'][0]['genres'])
            price = int(itunes_data['results'][0]['price'])
            artistName = itunes_data['results'][0]['artistName']
            artistId = int(itunes_data['results'][0]['artistId'])
            itunes_id = ItunesApple.objects.filter(artistId=artistId).first()
            if itunes_id:
                params = {
                    'data':itunes_id
                }
                return render(request, 'showdata.html', params)
            else:
                itunes_apple = ItunesApple(description=desc, genres=genres, price=price, artistName=artistName,
                artistId=artistId)
                itunes_apple.save()
                params = {
                    'data':ItunesApple.objects.get(artistId=artistId)
                }
                return render(request, 'showdata.html', params)
    return render(request, 'index.html')

def ShowData(request):

    return render(request, 'showdata.html')