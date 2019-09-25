from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.utils.text import slugify
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import user_passes_test
from notes.models import Note, Tag
from notes.forms import NoteForm, TagForm
from django.contrib.auth.decorators import user_passes_test
<<<<<<< HEAD

=======
>>>>>>> origin/master

def superuser_only(user):
    return user.is_authenticated and user.is_superuser



@user_passes_test(superuser_only, login_url="/")
def index_view(request):
<<<<<<< HEAD
    notes = Note.objects.all().order_by('-timestamp')
    tags = Tag.objects.all()
    return render(request, 'notes/index.html', {'notes': notes, 'tags': tags})


@user_passes_test(superuser_only, login_url="/")
def add_note(request):
    id = request.GET.get('id', None)
    if id is not None:
        note = Note.objects.get(id=id)
    else:
        note = None

    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Note Added!')
            return HttpResponseRedirect(reverse('notes.index'))

    else:
        form = NoteForm(instance=note)

    return render(request, 'notes/addnote.html', {'form': form})


@user_passes_test(superuser_only, login_url="/")
def add_tag(request):
    id = request.GET.get('id', None)
    if id is not None:
        tag = get_object_or_404(Tag, id=id)
    else:
        tag = None

    if request.method == 'POST':
        if request.POST.get('control') == 'delete':
            tag.delete()
            messages.add_message(request, messages.INFO, 'Tag Deleted!')
            return HttpResponseRedirect(reverse('notes:index'))

        form = TagForm(request.POST, instance=tag)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Tag Added!')
            return HttpResponseRedirect(reverse('notes:index'))

    else:
        form = TagForm(instance=tag)

    return render(request, 'notes/addtag.html', {'form': form, 'tag': tag})


=======
	notes = Note.objects.all().order_by('-timestamp')
	tags = Tag.objects.all()
	return render(request, 'notes/index.html', {'notes':notes, 'tags':tags})



@user_passes_test(superuser_only, login_url="/")
def add_note(request):
	id = request.GET.get('id', None)
	if id is not None:
		note = Note.objects.get(id=id)
	else:
		note = None
	
	if request.method == 'POST':
		form = NoteForm(request.POST, instance=note)
		if form.is_valid():
			form.save()
			messages.add_message(request, messages.INFO, 'Note Added!')
			return HttpResponseRedirect(reverse('notes:index'))
	
	else:
		form = NoteForm(instance=note)
		
	return render(request, 'notes/addnote.html', {'form':form})
	

@user_passes_test(superuser_only, login_url="/")
def add_tag(request):
	id = request.GET.get('id', None)
	if id is not None:
		tag = get_object_or_404(Tag, id=id)
	else:
		tag = None
	
	if request.method == 'POST':
		if request.POST.get('control') == 'delete':
			tag.delete()
			messages.add_message(request, messages.INFO, 'Tag Deleted!')
			return HttpResponseRedirect(reverse('notes:index'))
		
		form = TagForm(request.POST, instance=tag)
		if form.is_valid():
			form.save()
			messages.add_message(request, messages.INFO, 'Tag Added!')
			return HttpResponseRedirect(reverse('notes:index'))
	
	else:
		form = TagForm(instance=tag)
		
	return render(request, 'notes/addtag.html', {'form':form, 'tag':tag})
	
>>>>>>> origin/master
@user_passes_test(superuser_only, login_url="/")
def tag_search(request, **kwargs):
    slug = kwargs['slug']
    tag = get_object_or_404(Tag, slug=slug)
    notes = tag.notes.all()

    return render(request, 'notes/tagsearch.html', {'notes': notes, 'tag': tag})
