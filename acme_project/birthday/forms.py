from django import forms

from .models import Birthday

class BirthdayForm(forms.ModelForm):
    class Meta:
        # Указываем модель, на основе которой должна строиться форма.
        model = Birthday
        # Указываем, что надо отобразить все поля.
        fields = '__all__'
        widgets = {'description': forms.Textarea(attrs={'rows':5, 'cols':22}),'comment':forms.Textarea(attrs={'rows':5, 'cols':22})}
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        } 

