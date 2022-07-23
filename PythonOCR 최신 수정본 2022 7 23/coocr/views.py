from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
import os

from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = ''

def home(request):
    context = {}
    context['menutitle'] = 'HOME'

    return render(request, 'home.html', context)

def Local_food_recommend(request):
    context = {}
    context['menutitle'] = 'Local_food'

    return render(request, 'Local food recommend.html', context)

def taste_setting(request):
    return render(request, 'taste setting.html')

def upload_menu_board(request):
    context = {}
    context['menutitle'] = 'OCR READ'

    imgname = ''
    resulttext = ''
    if 'uploadfile' in request.FILES:
        uploadfile = request.FILES.get('uploadfile', '')

        if uploadfile != '':
            name_old = uploadfile.name
            name_ext = os.path.splitext(name_old)[1]

            fs = FileSystemStorage(location='static/source')
            imgname = fs.save(f"src-{name_old}", uploadfile)
            imgfile = Image.open(f"../static/source/{imgname}").convert('RGB')
            resulttext = pytesseract.image_to_string(imgfile, lang='kor')

    context['imgname'] = imgname
    context['resulttext'] = resulttext.replace(" ","")
    return render(request, 'upload menu board.html', context)

def Allergy_set(request):
    return render(request, 'Allergy setting.html')


