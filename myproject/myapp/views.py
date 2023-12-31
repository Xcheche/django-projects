from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {
        'name': 'Mary',
        'age': 31,
        'nationality': 'kenyan',
        'sex': 'female',
    }
    return render(request, 'index.html', context)


def counter(request):
    text = request.POST.get('text')
    amount_of_words = len(text.split())
    return render(request, 'counter.html', {'amount': amount_of_words})
