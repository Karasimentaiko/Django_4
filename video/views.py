from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UploadForm
from .models import FileUpload

# Upload
# upload("https://upload.wikimedia.org/wikipedia/commons/a/ae/Olympic_flag.jpg", public_id="olympic_flag")

# Transform
# url, options = cloudinary_url("olympic_flag", width=100, height=150, crop="fill")


def frontpage(request):
    return render(request, 'video/frontpage.html', {})


def upload(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/video')
    else:
        form = UploadForm()
    return render(request, 'video/upload.html', {'form': form})


def success(request):
    return render(request, 'video/success.html')
