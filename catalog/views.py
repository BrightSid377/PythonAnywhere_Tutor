
# copied over part of  Lib project  mjl 6/17/2024

from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Availability, Tutor, Subject, Session, Payment, Student, Parent_Guardian, EmergencyContact, \
    SessionInstance
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
    num_subjects = Subject.objects.all().count()
    num_availability = Availability.objects.all().count()


    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_tutors': num_tutors,
        'num_subjects': num_subjects,
        'num_availability': num_availability,
        }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'catalog/index.html', context=context)

from django.views import generic

class TutorListView(LoginRequiredMixin, generic.ListView):
    model = Tutor
class TutorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Tutor

class MySessionsByStudentListView (generic.ListView):
    model = SessionInstance
    template_name = 'catalog/my_session.html'
    paginate_by = 10

#    def get_queryset(self):
#        return SessionInstance.objects.filter\
#            (student_id=self.request.user)

#class BookListView(LoginRequiredMixin,generic.ListView):
#    model = Book

#class BookDetailView(LoginRequiredMixin,generic.DetailView):
#    model = Book


#class AuthorListView(LoginRequiredMixin,generic.ListView):
#    model = Author

#class AuthorDetailView(LoginRequiredMixin,generic.DetailView):
#    model = Author


# added the next two statements per class instructions
# to try to solve the Tutor image page load error mjl 6/22
class TutorCreate(CreateView):
    model = Tutor
    fields = ['tutor_id','tutor_fname','tutor_lname','tutor_address1','tutor_address2','tutor_city',\
              'tutor_state','tutor_zip','tutor_email','tutor_phone','tutor_hrRate','tutor_funFact',\
              'tutor_exp','tutor_image']

    def form_valid(self, form):
        post = form.save(commit=False)
        post.save()
        return HttpResponseRedirect(reverse('tutor_list'))

# mjl added 6/22
class TutorUpdate(UpdateView):
    model = Tutor
    fields = ['tutor_id','tutor_fname','tutor_lname','tutor_address1','tutor_address2','tutor_city',\
              'tutor_state','tutor_zip','tutor_email','tutor_phone','tutor_hrRate','tutor_funFact',\
              'tutor_exp','tutor_image']

    def form_valid(self, form):
        post = form.save(commit=False)
        post.save()
        return HttpResponseRedirect(reverse('tutor_list'))
...

