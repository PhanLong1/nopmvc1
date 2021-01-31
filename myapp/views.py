from django.shortcuts import render
from myapp.models import Student


def home(request):
        Data = {'Student' : Student.objects.all()}

        return render(request, 'pages/list.html',  Data)
