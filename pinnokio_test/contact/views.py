from django.shortcuts import render_to_response, get_object_or_404

from pinnokio_test.contact.models import Person


def index(request):
    my_person = get_object_or_404(Person, pk=1)
    return render_to_response('contact/index.html', {'person': my_person})
