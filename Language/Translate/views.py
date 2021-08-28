from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from translate import Translator


def index(request):
    return render(request, 'translate/index.html')

def translate(request):
    text = request.GET.get('translate')
    language = request.GET.get('language')
    translator= Translator(to_lang=language)
    translation = translator.translate(text)
    context = {
        "translation": translation
    }
    return JsonResponse(context)

"""
def translate(request):
    if request.method == "POST":
        text = request.POST["translate"]
        language = request.POST["language"]
        translator= Translator(to_lang=language)
        translation = translator.translate(text)
        return HttpResponse(translation)
        return render(request, "translate/translate.html")
"""

"""



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
"""
