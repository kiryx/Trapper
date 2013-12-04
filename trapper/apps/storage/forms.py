from ajax_select import make_ajax_field

from django import forms

from trapper.apps.animal_observation.models import Project
from trapper.apps.storage.models import Resource, Collection

class CollectionRequestForm(forms.Form):
	text = forms.CharField(widget=forms.Textarea)
	project = forms.ModelChoiceField(queryset=Project.objects.none())
	collection_pk = forms.IntegerField(widget=forms.HiddenInput())

class CollectionForm(forms.ModelForm):
	class Meta:
		model = Collection
	
	owner = make_ajax_field(Collection, 'owner', 'user', help_text=None, plugin_options={'autoFocus':True,})
	resources = make_ajax_field(Collection, 'resources', 'resource', help_text=None, show_help_text=False, plugin_options={'autoFocus':True,})
	managers = make_ajax_field(Collection, 'managers', 'user', help_text=None, show_help_text=False, plugin_options={'autoFocus':True,})

class ResourceForm(forms.ModelForm):
	class Meta:
		model = Resource
		# exclude the 'uploader' field as it is always the request.user
		exclude=['uploader', 'thumbnail', 'mime_type', 'resource_type']

	def save(self, force_insert=False, force_update=False, commit=True):
		r = super(ResourceForm, self).save(commit=False)
		if commit:
			r.save()
			r.update_metadata(commit=True)
		return r
	
	owner = make_ajax_field(Collection, 'owner', 'user', help_text=None, plugin_options={'autoFocus':True,})
	managers = make_ajax_field(Collection, 'managers', 'user', help_text=None, show_help_text=False, plugin_options={'autoFocus':True,})
