from django import forms
from .models import Memo 

class MemoForm(forms.Form):

    class Meta:
        model = Memo
        fields = ['title', 'description']
