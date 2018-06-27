from django import forms
from .models import Comment
import lxml.html

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('pseudo', 'email', 'contenu')

	def clean_contenu(self):
		contenu = self.cleaned_data['contenu']
		if lxml.html.fromstring(contenu).find('.//*') is not None:
			raise forms.ValidationError("Le commentaire ne peut pas contenir des balises HTML")

		return contenu

"""
class CommentForm(forms.Form):
	pseudo = forms.CharField(max_length=42, required=True)
	email = forms.EmailField(required=True)
	contenu = forms.CharField(widget=forms.Textarea, required=True)
"""