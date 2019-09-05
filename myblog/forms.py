from django import forms
from .models import ExampleModel

class MDEditorModleForm(forms.ModelForm):

    class Meta:
        model = ExampleModel
        fields = '__all__'