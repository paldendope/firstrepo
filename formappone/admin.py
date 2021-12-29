from django.contrib import admin
from formappone.models import StudentDetails

# Register your models here.
class StudentDetailsAdmin(admin.ModelAdmin):
    '''
        Admin View for StudentDetails
    '''
    list_display = ('usn','name','age','gender','course')
    

admin.site.register(StudentDetails, StudentDetailsAdmin)
