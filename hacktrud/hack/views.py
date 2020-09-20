from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .forms import *
from backend import HHParser
# Create your views here.
class index(ListView):

    parser = HHParser()

    def post(self, request):
    # if request.method =='POST':
        madel = request.POST['modelVac']
        print(self.parser.answer_questions('1ca17d2f00083b1a080039ed1f5042624d5234'))
        dir(madel)
        if (madel == 1): 
            
            return render(request, 'hack/person-form.html', {'form': personForm})
        elif madel == 2:
            personForm = personForm2()
            return render(request, 'hack/person-form.html', {'form': personForm})
        else:
            personForm = personForm3()
            return render(request, 'hack/person-form.html', {'form': personForm})
    # else:
    def get(self, request):       
        indexform = indexForm()
        return render(request, 'hack/base_form.html', {'form': indexform})


