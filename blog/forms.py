from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('pseudo', 'email', 'contenu')

"""
class CommentForm(forms.Form):
	pseudo = forms.CharField(max_length=42, required=True)
	email = forms.EmailField(required=True)
	contenu = forms.CharField(widget=forms.Textarea, required=True)
"""