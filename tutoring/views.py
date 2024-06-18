
# copied over part of  Lib project  mjl 6/17/2024

from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Availability, Tutor, Subject, Session, Payment, Student, Parent_Guardian, EmergencyContact
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView

from django.contrib import messages
from django.shortcuts import redirect

from django.http import HttpResponseRedirect
from django.urls import reverse

#from .forms import LoanBookForm
import datetime

# Create your views here.
def index(request):
    """View function for home page of site."""
    num_tutors = Tutor.objects.all().count()
    #num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    #num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    #num_authors = Author.objects.count()

    # Number of visits to this view, as counted in the session variable.
    #num_visits = request.session.get('num_visits', 0)
    #request.session['num_visits'] = num_visits + 1

    context = {
        'num_tutors': num_tutors,
    #    'num_instances': num_instances,
    #    'num_instances_available': num_instances_available,
    #    'num_authors': num_authors,
    #    'num_visits': num_visits,
        }
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

from django.views import generic

#class BookListView(LoginRequiredMixin,generic.ListView):
#    model = Book

#class BookDetailView(LoginRequiredMixin,generic.DetailView):
#    model = Book


#class AuthorListView(LoginRequiredMixin,generic.ListView):
#    model = Author

#class AuthorDetailView(LoginRequiredMixin,generic.DetailView):
#    model = Author
