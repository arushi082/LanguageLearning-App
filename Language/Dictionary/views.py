from django.shortcuts import render
from PyDictionary import PyDictionary


def index(request):
    return render(request, 'index.html')


# view for dictionary page
def dictionary(request):
    search = request.GET.get('search')
    dictionary1 = PyDictionary()
    meaning = dictionary1.meaning(search)
    synonyms = dictionary1.synonym(search)
    antonyms = dictionary1.antonym(search)
    context = {
        'meaning': meaning['Noun'][0],
        'synonyms': synonyms,
        'antonyms': antonyms
    }
    return render(request, 'dictionary/dictionary.html', context)
