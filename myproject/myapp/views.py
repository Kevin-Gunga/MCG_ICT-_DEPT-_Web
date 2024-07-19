from django.shortcuts import render
from .models import ApplyAttachment, Attendance, Report


# Create your views here.
def index(request):
    if request.method == 'POST':
         email = request.POST.get('email')   
         phone = request.POST.get('phone')
         department = request.POST.get('department')
         complain_txt = request.POST.get('complain_text')
         complain_fle = request.FILES.get('complain_file')
        
         new_report = Report(email_text=email, phone_number=phone, department_text=department, complain_text=complain_txt , complain_file=complain_fle)
         new_report.save()
                
    return render (request, 'myapp/index.html')
    

def attachees(request):
    if request.method == 'POST':
          first_name = request.POST.get('first_name')
          second_name = request.POST.get('second_name')
          surname = request.POST.get('surname')
          email_tt = request.POST.get('email')
          id_number = request.POST.get('id_number')
          institution_name = request.POST.get('institution_name')
          phone_n = request.POST.get('phone_num')
          documents = request.FILES.get('documents')
                
                     
          apply_attachment = ApplyAttachment(first_name=first_name ,second_name =second_name ,surname=surname, email=email_tt, id_number=id_number, institution_name=institution_name, phone_number=phone_n, documents=documents)   
          apply_attachment.save()
                 
                
                
    if request.method == 'POST':
          date_attend = request.POST.get('date')
          full_name = request.POST.get('full_nam')
          id = request.POST.get('id')
          time_in = request.POST.get('time_in')
          time_out = request.POST.get('time_out')
                     
          new_attendant = Attendance(date = date_attend, full_name=full_name, id_num=id, time_in=time_in, time_out=time_out)          
          new_attendant.save()
                       
                    
    if request.method == 'POST':
          email = request.POST.get('email')
          phone_num = request.POST.get('phone_num')
          department = request.POST.get('department')
          complain_txt = request.POST.get('complain_text')
          complain_fle = request.FILES.get('complain_file')
                        
          new_report = Report(email_text=email, phone_number=phone_num, department_text=department, complain_text=complain_txt , complain_file=complain_fle)
          new_report.save()
                       
                   
    return render (request, 'myapp/attachees.html')

