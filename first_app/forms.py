from django import forms
from first_app import models
 
 
class MembersForm(forms.ModelForm):
    class Meta:
        model = models.Members
        fields = "__all__"
        
        

    