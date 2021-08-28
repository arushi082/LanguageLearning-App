from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from PyDictionary import PyDictionary


def index(request):
    return render(request, 'dictionary/index.html')


# view for dictionary page
def dictionary(request):
    search = request.GET.get('search')
    dictionary = PyDictionary
    items = []
    meaning = dictionary.meaning(search)
    synonyms = dictionary.synonym(search)
    antonyms = dictionary.antonym(search)
    context = {
        'meaning': meaning,
        'synonyms': synonyms,
        'antonyms': antonyms
    }
    return JsonResponse(context)
