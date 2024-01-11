from django.shortcuts import render
from django.core.files.base import ContentFile
from .forms import QRCodeForm
from .models import QRCodeData
from .utils import generate_qr_code
from io import BytesIO

def home(request):
    return render(request, 'qrgenerator/home.html')

def qr_code_generator(request):
    if request.method == 'POST':
        form = QRCodeForm(request.POST)
        if form.is_valid():
            # data_text = form.cleaned_data['data_text']
            client_name = form.cleaned_data['client_name']
            service_provider = form.cleaned_data['service_provider']
            job_id = form.cleaned_data['job_id']

            combined_data = f"{client_name} {service_provider} {job_id}"

            # Save data to the database
            qr_code_data = QRCodeData.objects.create(data_text=combined_data)

            # Generate QR code using the utility function
            img = generate_qr_code(combined_data)

            # Save the QR code as an image in the model
            img_byte_array = BytesIO()
            img.save(img_byte_array, format="PNG")
            qr_code_data.qr_code_image.save('qrcode.png', ContentFile(img_byte_array.getvalue()))


            # Print the URL to the console
            print(f"QR Code Image URL: {qr_code_data.qr_code_image.url}")

            # Pass the QR code image to the template
            return render(request, 'qrgenerator/qr_code.html', {'img': qr_code_data})


    else:
        form = QRCodeForm()

    return render(request, 'qrgenerator/generator.html', {'form': form})
