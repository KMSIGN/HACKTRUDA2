from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from django.core.files.storage import FileSystemStorage
import csv
from io import StringIO
# Create your views here.
def index(request):
    if request.method =='POST':
        url = request.POST.get('url')
        file = request.POST.get('file')
        modelvac = request.POST.get('modelVac')
        myfile = request.FILES['file']
        csvf = StringIO(myfile.read().decode())
        reader = csv.reader(csvf, delimiter=',')

       ## with open(myfile, newline='') as f:
         #   reader = csv.reader(f)
         #   for row in reader:
          #      print(row)
           #     break

    #    with open('eggs.csv', newline='') as csvfile:
    ##        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
     #       for row in spamreader:
     #       print(', '.join(row))
        return render(request, 'hack/v.html', {'reader': reader})
    else:       
        indexform = indexForm()
        return render(request, 'hack/base_form.html', {'form': indexform})
