from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    stud_email = forms.EmailField( max_length=254, help_text='Required. Enter a valid email address.', label='Student Email Address')

    stud_first_name = forms.CharField(max_length=30, required=True, help_text='Required.', label='Student First Name')
    stud_last_name = forms.CharField(max_length=30, required=True, help_text='Required.', label='Student Last Name')
    stud_dob = forms.DateField(help_text='Required. Format: YYYY-MM-DD', label='Student Date of Birth')

    stud_address_line_1 = forms.CharField(max_length=255, required=True, label='Student Address Line 1')
    stud_address_line_2 = forms.CharField(max_length=255, required=False, label='Student Address Line 2')
    stud_city = forms.CharField(max_length=100, required=True, label='Student City')
    stud_state = forms.CharField(max_length=100, required=True, label='Student State')
    stud_zip_code = forms.CharField(max_length=10, required=True, label='Student Zip Code')

    under_18 = forms.BooleanField(required=False, label="Check Box if you are you under 18")

    parent_first_name = forms.CharField(max_length=30, required=False)
    parent_last_name = forms.CharField(max_length=30, required=False)
    parent_address_line_1 = forms.CharField(max_length=255, required=False)
    parent_address_line_2 = forms.CharField(max_length=255, required=False)
    parent_city = forms.CharField(max_length=100, required=False)
    parent_state = forms.CharField(max_length=100, required=False)
    parent_zip_code = forms.CharField(max_length=10, required=False)
    parent_email = forms.EmailField(max_length=254, required=False)

    emergency_contact_name = forms.CharField(max_length=255, required=False)
    emergency_contact_relationship = forms.CharField(max_length=255, required=False)
    emergency_contact_phone = forms.CharField(max_length=15, required=False)

    class Meta:
        model = User
        fields = ["username", "password1", "password2", 'under_18']

