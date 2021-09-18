from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import openpyxl 
import sys 
import glob
import os
import mimetypes
from django.core.files.temp import NamedTemporaryFile
import xlrd


from myapp.traitment.main import *
# Create your views here.
def index(request):
    return render(request,'index.html')

from django.conf import settings
from django.core.files.storage import FileSystemStorage

def simple_upload(request):
    #Deleting existing files 
    filelist = glob.glob('media/*')
    for f in filelist:
        os.remove(f)

    #Processing 
    if request.method == 'POST' and request.FILES['myfile']:
        
        #Reading files ....
        myfile = request.FILES['myfile']
        df=pd.read_excel(myfile)

        #Traitement
        dfs=traitement(df) 
        file_name=""
        file_extension=""
        file_name, file_extension = os.path.splitext(myfile.name)
        if file_extension==".xls":
            file_extension=".xlsx" 
        name_f="new_"+file_name+file_extension

        #Writing files and sheets ...
        writer=pd.ExcelWriter("media/"+name_f)
        print("après trajt")
        ls=[]
        colonnes_sheet=["Services","Équipements","Activités sur place","Types de clientèle","Conforts","Labels","Label"]

        dfs[0].to_excel(writer,sheet_name="Principal")
        dfs[1].to_excel(writer,sheet_name="Secondaire")
        writer.save()
        

        file_url="media/"+name_f
        
        if file_name!='':
            file_path=file_url
            print("nabil0")
            path = open(file_path, 'rb')
            print("nabil1")
            response = HttpResponse(path.read(), content_type='application/ms-excel; charset=utf-8')
            print("nabil")
            response['Content-Disposition'] = "attachment; filename=%s" % name_f
            return response
        else:
             return render(request,'index.html')

            

