from django.shortcuts import render
from googletrans import Translator,LANGUAGES
import pytesseract       
  
# adds image processing capabilities 
from PIL import Image     
  
 # converts the text to speech   
import pyttsx3 
# Create your views here.

def image_process(request):
    translator = Translator(service_urls=[
      'translate.google.com',
      'translate.google.co.kr',
    ])
    # ans = translator.translate('Hard',src='la')
    print(LANGUAGES)

    if request.POST:
        image = request.POST.get('image_file')
        img = Image.open(image)     
        # result = pytesseract.image_to_string(img)    
        print(img)
    return render(request,'index.html')