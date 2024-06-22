
# note mjl 6/17/2024 copied from lib project instructions
# updated to show

from django.contrib import admin
from .models import Availability, Tutor, Subject, Session, SessionInstance, Payment, Student, Parent_Guardian, EmergencyContact

admin.site.register(Availability)  # should be based on data models
admin.site.register(Tutor)
admin.site.register(Subject)
admin.site.register(Session)
admin.site.register(Payment)
admin.site.register(Student)
admin.site.register(Parent_Guardian)
admin.site.register(EmergencyContact)


@admin.register(SessionInstance)
class SessionInstanceAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'status', 'scheduled_date', 'session_id', 'id')
    list_filter = ('status', 'scheduled_date', 'session_id')

    fieldsets = (
        (None, {'fields': ('student_id', 'id', 'session_id')}),
        ('Session Status', {'fields': ('status', 'scheduled_date')}),
    )
