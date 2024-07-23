from django.shortcuts import render, redirect
from .forms import ImageUploadForm
from .models import UploadedImage

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_image = form.save()
            
            # Simulate LLM processing - replace with actual LLM API call
            description = "This is a simulated description from the LLM."
            uploaded_image.description = description
            uploaded_image.save()
            
            return redirect('show_image', pk=uploaded_image.pk)
    else:
        form = ImageUploadForm()
    return render(request, 'upload_image.html', {'form': form})

def show_image(request, pk):
    uploaded_image = UploadedImage.objects.get(pk=pk)
    return render(request, 'show_image.html', {'uploaded_image': uploaded_image})
