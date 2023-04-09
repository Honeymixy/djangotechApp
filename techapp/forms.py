from django import forms

class PostForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control w-50 '}))
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Enter description','class':'form-control w-50'}), required=True)
    image =forms.ImageField()
