from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from trapper.apps.animal_observation import views


urlpatterns = patterns('',
	# Home page of animal observation app
	url(r'^$', TemplateView.as_view(template_name='animal_observation/index.html'), name='index'),

	# Display project list and the details about given project
	url(r'project/list/$', views.ProjectListView.as_view(), name='project_list'),
	url(r'project/detail/(?P<pk>\d+)/$', views.ProjectDetailView.as_view(), name='project_detail'),
#	url(r'project/update/(?P<pk>\d+)/$', views.ProjectUpdateView.as_view(), name='project_update'),
	url(r'project/update/(?P<pk>\d+)/$', views.project_update, name='project_update'),
	url(r'project/create/$', views.ProjectCreateView.as_view(), name='project_create'),

	# FeatureSet views
	url(r'featureset/detail/(?P<pk>\d+)/$', views.FeatureSetDetailView.as_view(), name='featureset_detail'),
	url(r'featureset/list/$', views.FeatureSetListView.as_view(), name='featureset_list'),
	url(r'featureset/create/$', views.FeatureSetCreateView.as_view(), name='featureset_create'),
	url(r'featureset/update/(?P<pk>\d+)/$', views.FeatureSetUpdateView.as_view(), name='featureset_update'),

	# Feature views
	url(r'feature/detail/(?P<pk>\d+)/$', views.FeatureDetailView.as_view(), name='feature_detail'),
	url(r'feature/list/$', views.FeatureListView.as_view(), name='feature_list'),
	url(r'feature/create/$', views.FeatureCreateView.as_view(), name='feature_create'),
	url(r'feature/update/(?P<pk>\d+)/$', views.FeatureUpdateView.as_view(), name='feature_update'),

	# Display the classification form and process (action) it
	url(r'classify/(?P<project_id>\d+)/(?P<resource_id>\d+)/$', views.classify_resource, name='classify'),
	url(r'classify/action/$', views.process_classify, name='classify_action'),

	# Displays the details about given classification
	url(r'classification/details/(?P<pk>\d+)/$', views.classification_details, name='classification_details'),

	url(r'crowd/list/$', views.cs_resource_list, name='cs_resource_list'),
)
