from django.conf.urls import include, url
from django.contrib import admin
from notes.views import index_view, add_note, add_tag, tag_search

urlpatterns = [
	url(r'^$', index_view, name='index'),
	url(r'^addnote/', add_note, name='add_note'),
	url(r'^addtag/', add_tag, name='add_tag'),
	url(r'^tags/(?P<slug>[-\w]+)/$', tag_search, name='tagsearch'),
]