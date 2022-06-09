from django import forms


class PostText(forms.Form):
    title = forms.CharField(label='Post title', max_length=100)
    text = forms.CharField(label='Post text', max_length=100)


class Search(forms.Form):
    q = forms.CharField(label='Search', max_length=100)
