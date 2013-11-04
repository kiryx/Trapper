from django.conf.urls import patterns, include, url
from django.contrib import admin

from trapper import views

admin.autodiscover()

urlpatterns = patterns('',
	# Trapper homepage
    url(r'^$', views.index, name='trapper.index'),

	# Animal Observation urls
    url(r'^animal_observation/', include('trapper.apps.animal_observation.urls')),

	# Storage urls
    url(r'^storage/', include('trapper.apps.storage.urls')),

	# Accounts urls
    url(r'^accounts/', include('trapper.apps.accounts.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
