from django import forms
from .models import Career


class CareerForm(forms.ModelForm):
    fullname        = forms.CharField(max_length=200, widget=forms.TextInput(
        attrs={
        'class':'form-control form-control-sm mb-4'


        }))
    phone            = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={
        'class':'form-control form-control-sm mb-4'
        
        }))
    email            = forms.EmailField(max_length=255, widget=forms.EmailInput(
        attrs={
        'class':'form-control form-control-sm mb-4'
        
        }))
    education        = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={
        'class':'form-control form-control-sm mb-4 has-error'
        
        }))
    applying_for        = forms.CharField(max_length=200, widget=forms.TextInput(
        attrs={
        'class':'form-control form-control-sm mb-4'


        }))

    cover_letter = forms.CharField(widget=forms.Textarea(
        attrs={
        'class':'form-control form-control-sm mb-4 has-error',
        'rows':3
        
        }))
    cv               = forms.FileField(widget=forms.ClearableFileInput(
        attrs={
        'class':'form-control-file mb-4 has-error'
        
        }))


    class Meta:
        model = Career 

        fields = ('fullname','phone', 'email', 'education','applying_for', 'cover_letter','cv')