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
