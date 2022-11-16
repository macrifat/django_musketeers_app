from django.shortcuts import render
from first_app import forms
from first_app.models import Members
# Create your views here.


def index(request):
    member_list = Members.objects.order_by('last_name')
    diction = {'title': 'index', 'member_list': member_list }
    return render(request, 'first_app/index.html', context= diction)


def member_form(request):
    form = forms.MembersForm()
    
    if request.method == "POST":
        form = forms.MembersForm(request.POST)
        
        if form.is_valid():
            form.save(commit=True)
            return index(request)
    
    diction = {'title': 'member_form',"member_form": form } 
    return render(request, 'first_app/member_form.html', context= diction)

def member_info(request, member_id):
    member_info = Members.objects.get(pk=member_id)
    diction = {'member_info': member_info}
    return render(request, 'first_app/member_info.html', context=diction)

def member_update(request, member_id):
    member_info = Members.objects.get(pk=member_id)
    form = forms.MembersForm(instance=member_info)
     
    if request.method == 'POST':
        form = forms.MembersForm(request.POST, instance=member_info)
        
        if form.is_valid():
            form.save(commit=True)
            return index(request)
    
    diction = {'member_update': form }
    return render(request, 'first_app/member_update.html', context=diction)


def member_delete(request, member_id):
    member = Members.objects.get(pk=member_id).delete()
    diction = {'delete_msg': 'delete done'}
    return render(request, 'first_app/member_delete.html', context=diction)
