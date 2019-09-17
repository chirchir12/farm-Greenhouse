from django import forms


from .models import Contact
class ContactForm(forms.ModelForm):
    subject = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control'
    }))
    phone  = forms.CharField(label='Phone No.', widget=forms.TextInput(attrs={
        'class':'form-control'
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class':'form-control',
        'rows':'4'
    }))

    class Meta:
        model = Contact
        fields = ('subject', 'phone', 'message')

