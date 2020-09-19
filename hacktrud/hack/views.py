from django.shortcuts import render
from django.http import HttpResponse
from .forms import *

# Create your views here.
def index(request):
    if request.method =='POST':
        url = request.POST.get('url')
        file = request.POST.get('file')
        modelvac = request.POST.get('modelVac')
        return HttpResponse("<h1>форма отправлена</h1>")
    else:       
        indexform = indexForm()
        return render(request, 'hack/base_form.html', {'form': indexform})
