
# copied over part of  Lib project  mjl 6/17/2024

from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Availability, Tutor, Subject, Session, PaymentMethod, Student, Parent_Guardian, EmergencyContact, \
    SessionInstance, BillDetail
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

class TutorListView(generic.ListView):  #LoginRequiredMixin,
    model = Tutor
    context_object_name = "tutor_list"  # added 7/2/2024
    template_name = "catalog/tutor_list.html" # added 7/2/2024

class TutorDetailView(generic.DetailView):  #LoginRequiredMixin,
    model = Tutor
    # context_object_name = "tutor_detail" # added 7/2/2024
    # template_name = "catalog/tutor_detail.html" # added 7/2/2024


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
        # ...  # removed is this needed?

class BillDetailView(generic.DetailView):  #LoginRequiredMixin,
    model = BillDetail # added new bill details table  mjl 6/27/224
    # template_name = 'catalog/billing_details.html'
    # return render(request, 'catalog/billing_detaiis.html')

# class PaymentMethod(generic.CreateView):   # LoginRequiredMixin,
#   model = PaymentMethod
#    fields = ['payment_method','name_on_card','card_nbr','exp_date','cvv','pymt_acct_same',\
#    'pymt_addr1','pymt_addr2','pymt_city','pymt_state','pymt_zip']


class PaymentCreate(CreateView):
    model = PaymentMethod
    fields = ['payment_method','name_on_card','card_nbr','exp_date','cvv','pymt_acct_same',\
    'pymt_addr1','pymt_addr2','pymt_city','pymt_state','pymt_zip']

    def form_valid(self, form):
        post = form.save(commit=False)
        post.save()
        return HttpResponseRedirect(reverse('payment_details'))

class PaymentUpdate(UpdateView):
    model = PaymentMethod
    fields = ['payment_method', 'name_on_card', 'card_nbr', 'exp_date', 'cvv', 'pymt_acct_same', \
              'pymt_addr1', 'pymt_addr2', 'pymt_city', 'pymt_state', 'pymt_zip']
    def form_valid(self, form):
        post = form.save(commit=False)
        post.save()
        return HttpResponseRedirect(reverse('payment_details'))

# def payment_delete(request, pk):
#     payment = get_object_or_404(PaymentMethod, pk=pk)
#     try:
#         payment.delete()
#        messages.success(request, (payment.payment_method + " has been deleted"))
#    except:
#        messages.success(request, (payment.payment_method + ' cannot be deleted.'))
#    return redirect('payment_method')



