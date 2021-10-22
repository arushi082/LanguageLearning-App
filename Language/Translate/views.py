from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from Logging.logger import AppLogger
from translate import Translator

logger = AppLogger()

def index(request):
    """
      This function initiates the dictionary page
        :return: html
    """
    file_object = open("Translate_log.txt", 'a+')
    logger.log(file_object, 'Initiating Translation app', 'Info')
    return render(request, 'translate/index.html')

def translate(request):
    """
     This function translates English words or sentences into different languages and also pronounce it
        :return: html
    """
    try:
        text = request.GET.get('translate')
        inLang = request.GET.get('inlang')
        outLang = request.GET.get('outlang')
        translator= Translator(to_lang=outLang ,from_lang = inLang)
        translation = translator.translate(text)
        print(translation)
        context = {
            "translation": translation
        }
        file_object = open("Translate_log.txt", 'a+')
        logger.log(file_object, 'Translates words or sentences into diff languages using translate library', 'Info')
        file_object.close()
        return JsonResponse(context)
    except Exception as e:
        logger.log(
            file_object,
            f'Exception occured in translating . Message: {str(e)}',
            'Error')
        file_object.close()
