from django.shortcuts import render

# Create your views here.

# view for dictionary page
def dictionary(request):
    return render(request=request, template_name='dictionary/dictionary.html')
