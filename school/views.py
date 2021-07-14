from django.shortcuts import render
from .models import Student


# Create your views here.

def home(request):
    students_data = Student.objects.all()
    s1_data = Student.objects.filter(marks=999)
    s2_data = Student.objects.exclude(marks=999)
    s3_data = Student.objects.order_by('marks')
    s31_data = Student.objects.order_by('-marks')
    s32_data = Student.objects.order_by('?')
    s4_data = Student.objects.order_by('roll_no').reverse()
    s41_data = Student.objects.order_by('roll_no').reverse()[:5]
    s5_data = Student.objects.values()
    """ gives return in dictionary format"""
    print(s5_data)
    s51_data = Student.objects.values('name', 'city')
    print(s51_data)
    return render(request, 'school/home.html', {'students_data': students_data, 's1_data': s1_data, 's2_data':s2_data,
                                                's3_data':s3_data,'s31_data':s31_data, 's32_data':s32_data,
                                                's4_data':s4_data,'s41_data':s41_data,'s5_data':s5_data,
                                                's51_data':s51_data})
