from django import forms

class ContactForm(forms.Form):
    Name = forms.CharField(label='NAME', required=True, max_length=50)
    Email = forms.EmailField(label='EMAIL', required=True, max_length=50)
    Subject = forms.CharField(label='SUBJECT', required=True, max_length=50)
    Content = forms.CharField(label='CONTENT', required=False, max_length=50, widget=forms.Textarea)

