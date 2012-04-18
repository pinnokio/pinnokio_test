from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.template.context import RequestContext

from pinnokio_test.contact.models import Person
from pinnokio_test.contact.forms import PersonEditForm


def index(request):
    my_person = get_object_or_404(Person, pk=1)
    return render_to_response('contact/index.html',
                              {'person': my_person},
                              context_instance=RequestContext(request))

def contact_edit(request):
    home_url = reverse('index')
    my_person = get_object_or_404(Person, pk=1)
    form = PersonEditForm(request.POST or None,
                          request.FILES or None,
                          instance=person)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render_to_response('contact/edit.html',
                              {'form': form,
                               'next': request.GET.get('next', home_url)},
                               context_instance=RequestContext(request))
