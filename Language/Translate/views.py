from django.shortcuts import render

# Create your views here.

# view for translate page
def translate(request):
    return render(request=request, template_name='translate/translate.html')
