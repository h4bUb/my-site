from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # exclude = ['author', 'updated', 'created', ]
        fields = ['author', 'text']
        widgets = {
        	'author': forms.TextInput(
                attrs={'id': 'post-author', 'required': True, 'placeholder': 'Who are you?'}
            ),
            'text': forms.TextInput(
                attrs={'id': 'post-text', 'required': True, 'placeholder': 'Speak'}
            ),
        }


class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control input-sm'}))
    email = forms.EmailField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control input-sm'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control input-sm'}), max_length=1000)

    class Meta:
    	model = Post
    	fields = ('author', 'text',)