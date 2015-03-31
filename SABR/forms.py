from django import forms
from SABR.models import Batting, Master




    
class MasterForm(forms.Form):
    nameFirst = forms.CharField(max_length=128, help_text="Please enter the category name.")
    

    class Meta:
        model = Master
       