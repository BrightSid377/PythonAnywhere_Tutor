
# note mjl 6/17/2024 modified from lib project

from django.db import models
# from django.urls import reverse
import uuid

from django.contrib.auth.models import User
# from datetime import date

# examples of various types from lib project  mjl 6/17/2024
# https://docs.djangoproject.com/en/5.0/topics/db/models/
# id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular bohole library')
# author = models.ForeignKey('Author', on_delete=models.RESTRICT, null=True)
# title = models.CharField(max_length=200)
# summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
# date_of_birth = models.DateField(null=True, blank=True)
# date_of_death = models.DateField('Died', null=True, blank=True)
# author_image = models.ImageField(upload_to='images/', null=True, blank=True)
# genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')


class Availability(models.Model):
    availability_id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for available times')
    avail_day = models.DateField(null=True, blank=True)
    avail_time = models.TimeField(null=True, blank=True)
    tutor_id = models.ForeignKey('Tutor', on_delete=models.RESTRICT, null=True)

    def __str__(self):
        # return self.availability_id
        return f'{self.avail_day}, {self.avail_time}'


class Subject(models.Model):
    subject_id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for subjects')
    subject_category = models.CharField(max_length=200)
    subject_level = models.CharField(max_length=200)
    subject_name = models.CharField(max_length=200)
    tutor_id = models.ForeignKey('Tutor', on_delete=models.RESTRICT, null=True)

    def __str__(self):
        return self.subject_name


class EmergencyContact(models.Model):
    emcont_id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for Emergency Contact')
    emcont_name = models.CharField(max_length=200)
    emcont_relationship = models.CharField(max_length=200)
    emcont_phone = models.CharField(max_length=20)

    def __str__(self):
        return self.emcont_name


class Payment(models.Model):
    payment_id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for Payments')
    payment_amount = models.IntegerField()
    payment_method = models.CharField(max_length=200)
    student_id = models.ForeignKey('Student', on_delete=models.RESTRICT, null=True)
    session_id = models.ForeignKey('Session', on_delete=models.RESTRICT, null=True)

    def __str__(self):
        return self.payment_amount


class Session(models.Model):
    session_id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for a Session')
    session_date = models.DateField(null=True, blank=True)
    session_duration = models.IntegerField()
    session_time = models.TimeField(null=True, blank=True)
    session_location = models.CharField(max_length=200)
    student_id = models.ForeignKey('Student', on_delete=models.RESTRICT, null=True)
    tutor_id = models.ForeignKey('Tutor', on_delete=models.RESTRICT, null=True)

    def __str__(self):
        # return self.EmCont_name
        return f'{self.session_date}, {self.session_time}'


class Tutor(models.Model):
    tutor_id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for a Tutor')
    tutor_fname = models.CharField(max_length=100)
    tutor_lname = models.CharField(max_length=100)
    tutor_address1 = models.CharField(max_length=250)
    tutor_address2 = models.CharField(max_length=250)
    tutor_city = models.CharField(max_length=100)
    tutor_state = models.CharField(max_length=100)
    tutor_zip = models.IntegerField()
    tutor_email = models.EmailField(max_length=100)
    tutor_phone = models.CharField(max_length=20)
    tutor_hrRate = models.IntegerField()
    tutor_funFact = models.TextField(max_length=1000, help_text='Enter a fun fact about yourself')
    tutor_exp = models.IntegerField()

    class Meta:
        ordering = ['tutor_lname', 'tutor_fname']

    def __str__(self):
        return f'{self.tutor_lname}, {self.tutor_fname}'


class Parent_Guardian(models.Model):
    parent_id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for Parent or Guardian')
    parent_fname = models.CharField(max_length=100)
    parent_lname = models.CharField(max_length=100)
    parent_address1 = models.CharField(max_length=250)
    parent_address2 = models.CharField(max_length=250)
    parent_city = models.CharField(max_length=100)
    parent_state = models.CharField(max_length=100)
    parent_zip = models.IntegerField()
    parent_email = models.EmailField(max_length=100)
    parent_phone1 = models.CharField(max_length=20)
    parent_phone2 = models.CharField(max_length=20)

    class Meta:
        ordering = ['parent_lname', 'parent_fname']

    def __str__(self):
        return f'{self.parent_lname}, {self.parent_fname}'


class Student(models.Model):
    student_id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for a Student')
    student_fname = models.CharField(max_length=100)
    student_lname = models.CharField(max_length=100)
    student_address1 = models.CharField(max_length=250)
    student_address2 = models.CharField(max_length=250)
    student_city = models.CharField(max_length=100)
    student_state = models.CharField(max_length=100)
    student_zip = models.IntegerField()
    student_email = models.EmailField(max_length=100)
    student_phone = models.CharField(max_length=20)
    student_dob = models.DateField(null=True, blank=True)
    parent_id = models.ForeignKey('Parent_Guardian', on_delete=models.RESTRICT, null=True)
    emcont_id = models.ForeignKey('EmergencyContact', on_delete=models.RESTRICT, null=True)

    class Meta:
        ordering = ['student_lname', 'student_fname']
    # def get_absolute_url(self):
    #    """Returns the URL to access a detail record for this book."""
    #    return reverse('student_detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.student_lname}, {self.student_fname}'
