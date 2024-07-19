from django.utils import timezone
from django.db import models

# Create your models here.
class Report(models.Model):
    email_text = models.EmailField(max_length=254, default='email', null= True, blank= True)
    phone_number = models.CharField(max_length=15, default='phone', null= True, blank= True)
    department_text = models.CharField(max_length=15,default='department', null= True, blank= True)
    complain_text = models.TextField(default='complaints',null=True)
    complain_file = models.FileField(verbose_name='Complaint File', default='complaints', null=True, blank=True)
    
    def __str__(self):
        return self.department_text  
    
class ApplyAttachment(models.Model):
    first_name = models.CharField(max_length=30, default='first_name', null=True, blank=True)
    second_name = models.CharField(max_length=30, default='second_name', null=True ,blank=True)
    surname = models.CharField(max_length=30, default='surname', null=True, blank=True)
    email = models.EmailField(max_length=254, default='email', null=True, blank=True)
    id_number = models.CharField(max_length=10, default='id_number', null=True, blank=True)
    institution_name = models.CharField(max_length=254, default='institution_name', null=True, blank=True)
    phone_number = models.CharField(max_length=15, default='phone_number', null=True, blank=True)
    documents = models.FileField(verbose_name='documents', default='documents', null=True, blank=True)
    
    def __str__(self):
        return f'{self.first_name} {self.second_name}'
    
def current_time():
    return timezone.now().time()
class Attendance(models.Model):
    date = models.DateField("date attended",null=True, default=timezone.now)
    full_name = models.CharField(max_length=30, null=True, default='full_name', blank=True)
    id_num = models.CharField(max_length=15, null=True, default='id_num', blank=True)
    time_in = models.TimeField("time in", null=True, blank=True, default=current_time)
    time_out = models.TimeField("time out", null=True, blank=True,default=current_time)
    
    def date_attended(self):
        return self.date 
    
    def __str__(self):
        return self.full_name if self.full_name else 'Unnamed Attendee'
    
    def time(self):
        return f'{self.time_in} {self.time_out}'