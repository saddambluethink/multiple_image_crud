
from django.shortcuts import redirect, render, HttpResponse
from .models import mlimagemodel,mlimage,Imagepath
from django.core.files.storage import FileSystemStorage
# Create your views here.
                           
#multiple image upload


def imageurls(request):
    if request.method=="POST":
        image=request.FILES.getlist('images')
        fs = FileSystemStorage()
        i=""
        for img in image:
            file_url = fs.save(img.name, img)
            imgpath = fs.url(file_url)
            if '%20' in imgpath:
                imgpath = str(imgpath).replace("%20", " ")
            #print(fs.url(file_url),"path here--------------")
            i += str(imgpath) + ','
        i = i[:-1]
        print(i, "------------")
        obj=Imagepath(imname=i)
        obj.save()
        print("data saved")
        # print(i)
        # print(type(i))
        # print("urlist end")
    img=Imagepath.objects.all()
    b=[]
    for i in img:
        a=i.imname
        b.extend(a.split(','))
        
    print("my list-------------------------------------------------")   
    print(b) 
    
    return render(request,'urlimage.html',{'images':b})


def showimage(request):

    img=Imagepath.objects.all()
    
    
    d={}
    for i in img:
        b=[]
        a=i.imname
        b= b + a.split(',')
        # b.pop()
        
        d[f"{i.id}"]=b  
      
    return render(request,'urldelete.html',{'images':d})



def deleteimg(request):
    if request.method=='POST':
        id=request.POST.get('id')
        x=request.POST.get('imagename')
        ft=Imagepath.objects.get(id=id)
        l=ft.imname
        b=l.split(',')
        
        if x in b:
            b.remove(x)
        
        b = ",".join(b)
        print("deleted")
        ft.imname = b
        ft.save()
        return redirect('/show')


def updateimg(request):
    print("updated-------------------------------------------")
    if request.method=='POST':
        id=request.POST.get('id')
        x=request.POST.get('upimage')

        upimage=request.FILES.get('images')
        print(upimage,x,"-------------------------------------")
        fs = FileSystemStorage()
        
        file_url = fs.save(upimage.name, upimage)
        imgpath = fs.url(file_url)
        
        print("------------------------------------------------------------")
        print(imgpath)
        print(id)
        print(x)
        if '%20' in imgpath:
            imgpath = str(imgpath).replace('%20', ' ')
       
        ft=Imagepath.objects.get(id=id)
        l=ft.imname
        print(l,"--------------------")
        b=l.split(',')
        print(b,"-----b-----b-------b")
        if x in b:
            #b.remove(x)
            c=b.index(x)
            b[c]=imgpath 
       # b.append(imgpath)
        data = ",".join(b)
        print(data, "------#########################---------s")
        ft.imname = data
        ft.save()
        return redirect('/show')
