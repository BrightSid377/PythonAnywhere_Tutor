# RET checking that the version control works
# RT Edited some functions and required values of attributes
# note mjl 6/17/2024 modified from lib project


from django.db import models
from django.urls import reverse
import uuid
from django.contrib.auth.models import User
from datetime import date

Time_Choice = (
    ('9-10', '09:00 - 10:00'),
    ('10-11', '10:00 - 11:00'),
    ('11-12', '11:00 - 12:00'),
    ('12-1', '12:00 - 13:00'),
    ('1-2', '13:00 - 14:00'),
    ('2-3', '14:00 - 15:00'),
    ('3-4', '15:00 - 16:00'),
    ('4-5', '16:00 - 17:00'),
)

Days_Choice = (
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
    ('Sunday', 'Sunday'),
)


class Availability(models.Model):
    availability_id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for available times')
    avail_day = models.CharField(max_length=9, choices=Days_Choice, null=True, blank=True)
    avail_time = models.CharField(max_length=13, choices=Time_Choice, null=True, blank=True)
    tutor_id = models.ForeignKey('Tutor', on_delete=models.RESTRICT, null=True)

    def __str__(self):
        # return self.availability_id
        return f'{self.avail_day}, {self.avail_time}'


class Subject(models.Model):
    subject_id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for subjects')
    subject_category = models.CharField(max_length=50)
    subject_level = models.CharField(max_length=50)
    subject_name = models.CharField(max_length=50)
    tutor_id = models.ForeignKey('Tutor', on_delete=models.RESTRICT, null=True)

    def __str__(self):
        return self.subject_name


class EmergencyContact(models.Model):
    emcont_id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for Emergency Contact')
    emcont_name = models.CharField(max_length=50)
    emcont_relationship = models.CharField(max_length=20)
    emcont_phone = models.CharField(max_length=10)

    def __str__(self):
        return self.emcont_name


class PaymentMethod(models.Model):
    # pymt_method_id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for Payment Method')
    # payment_amount = models.IntegerField() # will be calculated based on duration and tutor rate
    payment_method = models.CharField(max_length=200)
    # added new fields for payment screen mjl 6/27/2024
    name_on_card = models.CharField(max_length=200, default="none")
    card_nbr = models.IntegerField(default=0)
    exp_date = models.CharField(max_length=20, default="01/24")  # will be 2 digit month and year
    cvv = models.IntegerField(default=0)
    pymt_acct_same = models.BooleanField()  # for checkbox to indicate if same as student address
    pymt_addr1 = models.CharField(max_length=200)
    pymt_addr2 = models.CharField(max_length=200)
    pymt_city = models.CharField(max_length=200)
    pymt_state = models.CharField(max_length=200)
    pymt_zip = models.IntegerField()
    # end of new fields added 6/27
    student_id = models.ForeignKey('Student', on_delete=models.RESTRICT, null=True)
    # shouldn't need this session id, will connect thorugh bill details mjl 7/2
    # session_id = models.ForeignKey('Session', on_delete=models.RESTRICT, null=True)

    def __str__(self):
        return str(self.pymt_method_id)

    def get_absolute_url(self):
        return reverse('payment_create', args=[str(self.id)])


# this table to represent the invoice that the custom would be presented mjl 7/2
class BillDetail(models.Model):
    # bill_id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for Bill Address')
    bill_num = models.IntegerField(default = 12345)
    bill_date = models.CharField(max_length=20,default = '07/02/2024')
    #bill_city = models.CharField(max_length=200)
    #bill_state = models.CharField(max_length=200)
    # removing link to payment method, will address separately mjl 7/2
    # pymt_method_id = models.ForeignKey('PaymentMethod', on_delete=models.RESTRICT, blank=True, null=True)
    session_id = models.ForeignKey('Session', on_delete=models.RESTRICT, blank=True, null=True)

    #def get_absolute_url(self):
    #    """Returns the URL to access a particular author instance."""
    #    return reverse('billing_details', args=[str(self.bill_id)])

    def get_absolute_url(self):
        return reverse('billing_details', args=[str(self.id)])

    def __str__(self):
        return str(self.bill_num)




class Session(models.Model):
    session_id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for a Session')
    session_date = models.DateField(null=True, blank=True)
    session_duration = models.IntegerField()
    session_time = models.CharField(max_length=13, choices=Time_Choice, null=True, blank=True)
    session_location = models.CharField(max_length=200)
    student_id = models.ForeignKey('Student', on_delete=models.RESTRICT, null=True)
    tutor_id = models.ForeignKey('Tutor', on_delete=models.RESTRICT, null=True)

    def __str__(self):
        # return self.EmCont_name
        return f'{self.session_date}, {self.session_time}'


class SessionInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for a Particular Session')
    session_id = models.ForeignKey('Session', on_delete=models.RESTRICT, null=True)
    scheduled_date = models.DateField(null=True, blank=True)

    SESSION_STATUS = (('c', 'Completed'), ('t', 'Tardy'), ('ns', 'No Show'), ('a', 'Absent'), ('s', 'Scheduled'),)
    status = models.CharField(max_length=2, choices=SESSION_STATUS, blank=True, default='s', help_text='Session status')

    student_id = models.ForeignKey('Student', on_delete=models.SET_NULL, null=True, blank=True)

    @property
    def booked_session(self):
        return bool(self.scheduled_date and date.today() > self.scheduled_date)

    class Meta:
        ordering = ['scheduled_date']

    def get_absolute_url(self):
        """Returns the URL to access a particular author instance."""
        return reverse('my_session', args=[str(self.id)])

    def __str__(self):
        return f'{self.id}, {self.scheduled_date}'


class Tutor(models.Model):
    # tutor_id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for a Tutor')
    tutor_fname = models.CharField(max_length=50)
    tutor_lname = models.CharField(max_length=50)
    tutor_address1 = models.CharField(max_length=150)
    tutor_address2 = models.CharField(max_length=50, blank=True, null=True)
    tutor_city = models.CharField(max_length=50)
    tutor_state = models.CharField(max_length=2)
    tutor_zip = models.IntegerField()
    tutor_email = models.EmailField(max_length=100)
    tutor_phone = models.CharField(max_length=10)
    tutor_hrRate = models.DecimalField(max_digits=4, decimal_places=2)
    tutor_funFact = models.TextField(max_length=1000, help_text='Enter a fun fact about yourself')
    tutor_exp = models.DecimalField(max_digits=3, decimal_places=1, help_text="Enter the amount of expenses you have")
    tutor_image = models.ImageField(upload_to='images/', null=True, blank=True)

    class Meta:
        ordering = ['tutor_lname', 'tutor_fname']

    def get_absolute_url(self):
        return reverse('tutor_detail', args=[str(self.id)])
        # trying self id mjl 7/2/2024

    def __str__(self):
        return f'{self.tutor_lname}, {self.tutor_fname}'

    # return render(request=request,template_name="tutor_detail.html")


class Parent_Guardian(models.Model):
    parent_id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for Parent or Guardian')
    parent_fname = models.CharField(max_length=50)
    parent_lname = models.CharField(max_length=50)
    parent_address1 = models.CharField(max_length=150)
    parent_address2 = models.CharField(max_length=50, blank=True, null=True)
    parent_city = models.CharField(max_length=50)
    parent_state = models.CharField(max_length=2)
    parent_zip = models.IntegerField()
    parent_email = models.EmailField(max_length=100)
    parent_phone1 = models.CharField(max_length=10)
    parent_phone2 = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        ordering = ['parent_lname', 'parent_fname']

    def __str__(self):
        return f'{self.parent_lname}, {self.parent_fname}'


class Student(models.Model):
    student_id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for a Student')
    student_fname = models.CharField(max_length=50)
    student_lname = models.CharField(max_length=50)
    student_address1 = models.CharField(max_length=150)
    student_address2 = models.CharField(max_length=100, blank=True, null=True)
    student_city = models.CharField(max_length=100)
    student_state = models.CharField(max_length=2)
    student_zip = models.IntegerField()
    student_email = models.EmailField(max_length=100, blank=True, null=True)
    student_phone = models.CharField(max_length=10, blank=True, null=True)
    student_dob = models.DateField(null=True, blank=False)
    parent_id = models.ForeignKey('Parent_Guardian', on_delete=models.RESTRICT, blank=True, null=True)
    emcont_id = models.ForeignKey('EmergencyContact', on_delete=models.RESTRICT, blank=True, null=True)
    # removing pointer to bill detail table , will go via sessions to find and calculate bills
    # bill_id = models.ForeignKey('BillDetail', on_delete=models.RESTRICT, blank=True, null=True)

    class Meta:
        ordering = ['student_lname', 'student_fname']

    # def get_absolute_url(self):
    #    """Returns the URL to access a detail record for this book."""
    #    return reverse('student_detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.student_lname}, {self.student_fname}'
