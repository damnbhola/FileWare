from datetime import timedelta

from django.shortcuts import render, redirect, get_object_or_404
from .models import File
from django.utils import timezone


def home(request):
    try:
        if request.method == 'POST' and request.FILES['myfile']:
            uploaded_file = request.FILES['myfile']
            date = date_time()
            file = File(file=uploaded_file, file_name=uploaded_file.name, up_date=date)
            file.save()
            uploaded_file_url = f"/file/{file.location}"
            return render(request, 'upload.html', {
                'uploaded_file_url': uploaded_file_url
            })
    except Exception as e:
        print(e)
    return render(request, 'upload.html')


def detail(request, location):
    file = get_object_or_404(File, location=location)
    return render(request, 'detail.html', {'file': file})


def file_list(request):
    files = File.objects.all()
    return render(request, 'file_list.html', {
        'files': files
    })


def delete_file(request, pk):
    if request.method == 'POST':
        file = File.objects.get(pk=pk)
        file.delete()
    return redirect('file_list')


def date_time():
    return timezone.now() + timedelta(hours=5, minutes=30)
