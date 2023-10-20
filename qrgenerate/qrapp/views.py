from django.shortcuts import render, redirect
from django.http import FileResponse
from django.urls import reverse
from qrapp.form import qrform
from qrapp.models import qr
from io import BytesIO
import qrcode, os, base64

# Create your views here.

def generate_qr_code(request):
    qr_code = None
    if request.method == "POST":
        fm = qrform(request.POST)
        if fm.is_valid():
            name =  fm.cleaned_data["name"]
            text = fm.cleaned_data['text']
            ls = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
            ls.add_data(text)
            ls.make(fit=True)

            img = ls.make_image(fill_color="black", back_color="white")
            buffer = BytesIO()
            img.save(buffer)
            qr_code = base64.b64encode(buffer.getvalue()).decode("utf-8")
            key = qr(name=name, text=text)
            key.save()
            return render(request, 'qrapp/index.html', {'form': fm, 'qr_code': qr_code})
    else:
        fm = qrform()
    return render(request, 'qrapp/index.html', {'form': fm})

def download_qr_code(request):
    qr_code_path = os.path.join(os.getcwd(), 'qrcode.png')
    response = FileResponse(open(qr_code_path, 'rb'))
    response['Content-Type'] = 'image/png'
    response['Content-Disposition'] = f'attachment; filename="{os.path.basename(qr_code_path)}"'
    return response    
