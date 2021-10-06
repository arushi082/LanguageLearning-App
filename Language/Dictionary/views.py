from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from PyDictionary import PyDictionary
from Logging.logger import AppLogger

logger = AppLogger()

def index(request):
    """
       This function initiates the dictionary page
       :return: html
       """
    file_object = open("Dictionary_log.txt", 'a+')
    logger.log(file_object, 'Initiating app', 'Info')
    return render(request, 'dictionary/index.html')


# view for dictionary page
def dictionary(request):
    """
     This function searches for the words using PyDictionary
    :return: html
    """
    try:
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
        file_object = open("Dictionary_log.txt", 'a+')
        logger.log(file_object, 'Searches for meaning Synonmys and Antonyms', 'Info')
        file_object.close()
        return JsonResponse(context)
        logger.log(file_object, 'Prints Meaning of searched word', 'Info')
        file_object.close()
    except Exception as e:
        logger.log(
            file_object,
            f'Exception occured in searching meaning. Message: {str(e)}',
            'Error')
        file_object.close()

