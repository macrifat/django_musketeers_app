from django.shortcuts import render

# Create your views here.


def index(request):
    diction = {'title': 'index'}
    return render(request, 'first_app/index.html', context= diction)


def member_form(request):
    diction = {'title': 'member_form'}
    return render(request, 'first_app/member_form.html', context= diction)