from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Articles
#from .forms import UploadFileForm


# Create your views here.
def index(request):
    data = {
        'title': 'Bosh sahifa'
    }
    return render(request, 'main/index.html', data)

def ikki_suz(request):
    #if request.method == 'post':
        #form = UploadFileForm(request.POST, request.FILES)

    return render(request, 'main/ikki_suz.html')

def uch_suz(request):
    return render(request, 'main/uch_suz.html')

def turt_suz(request):
    suz_birikma = Articles.objects.order_by('-date')[:1]
    return render(request, 'main/turt_suz.html')