from django import forms
from.models import student
from.models import reportcard
from.models import position

class studentform(forms.ModelForm):
    class Meta:
        model=student
        fields='__all__'
        
class reportcardform(forms.ModelForm):
    class Meta:
        model=reportcard
        fields='__all__' 
        
class positionform(forms.ModelForm):
    class Meta:
        model=position
        fields='__all__'       