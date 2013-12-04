from django import forms
from trapper.apps.messaging.models import Message
from tinymce.widgets import TinyMCE

class MessageForm(forms.ModelForm):
	class Meta:
		model = Message

	text = forms.CharField(widget=TinyMCE(attrs={'cols':60, 'rows':15}))