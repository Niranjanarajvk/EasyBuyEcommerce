from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from APP1.models import categorydb,westernwomendb,westernmendb,Accessoriesdb,adminpagedb,productdatabase,Contactdb,Blogdb
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User

# Create your views here.
def indexpage(request):
    return render(request,'index.html')

def categorypage(request):
    return render(request,'category.html')

def categorypagedb(request):
    if request.method=="POST":
        na=request.POST.get('name')
        br=request.POST.get('brand')
        de=request.POST.get('desc')
        img = request.FILES['image']
        obj =categorydb(CategoryName=na,Brand=br,Description=de,Image=img)
        obj.save()
        return  redirect(categorypage)

def displaycategory(request):
    data = categorydb.objects.all()
    return render(request,'displaycategory.html',{'data':data})
def editcategorypage(request,dataid):
    data =categorydb.objects.get(id=dataid)
    print(data)
    return render(request,'editcategory.html',{'data':data})
def updatecategorypage(request,dataid):
    if request.method=="POST":
        na = request.POST.get('name')
        br = request.POST.get('brand')
        de = request.POST.get('desc')

        try:
            img =request.FILES['image']
            fs =FileSystemStorage()
            file=fs.save(img.name, img)
        except MultiValueDictKeyError:
            file=categorydb.objects.get(id=dataid).Image
        categorydb.objects.filter(id=dataid).update(CategoryName=na,Brand=br,Description=de,Image=file)
        return redirect(displaycategory)

def deletecategory(request,dataid):
    data=categorydb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaycategory)


def westernpage(request):
    return render(request,'Womenfashion.html')

def westwomendb(request):
    if request.method=="POST":
        na=request.POST.get('name')
        co=request.POST.get('code')
        pr=request.POST.get('price')
        img = request.FILES['image']

        obj = westernwomendb(DressName=na,Code=co,Price=pr,Image=img)
        obj.save()
        return  redirect(westernpage)

def displaypage(request):
    data = westernwomendb.objects.all()
    return render(request,'displaywomen.html',{'data':data})

def editpage(request,dataid):
    data = westernwomendb.objects.get(id=dataid)
    print(data)
    return render(request,'editwomen.html', {'data':data})

def updatewesterndata(request,dataid):
    if request.method=="POST":
        na = request.POST.get('name')
        pr = request.POST.get('price')
        co = request.POST.get('code')

        try:
            img =request.FILES['image']
            fs =FileSystemStorage()
            file=fs.save(img.name, img)
        except MultiValueDictKeyError:
            file=westernwomendb.objects.get(id=dataid).Image
        westernwomendb.objects.filter(id=dataid).update(DressName=na,Code=co,Price=pr,Image=file)
        return redirect(displaypage)


def deletedata(request,dataid):
    data=westernwomendb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaypage)


def westmen(request):
    return render(request,'Menfashion.html')

def westmendb(request):
    if request.method=="POST":
        na = request.POST.get('name')
        co = request.POST.get('code')
        pr = request.POST.get('price')
        img = request.FILES['image']

        obj = westernmendb(DressName=na, Code=co, Price=pr, Image=img)
        obj.save()
        return redirect(westernpage)

def displaymen(request):
    data=westernmendb.objects.all()
    return render(request,'displaymen.html',{'data':data})

def editmen(request,dataid):
    data=westernmendb.objects.get(id=dataid)
    print(data)
    return render(request,'editmenfashion.html',{'data':data})

def updatemenfasion(request,dataid):
    if request.method=="POST":
        na = request.POST.get('name')
        co = request.POST.get('code')
        pr = request.POST.get('price')
        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            file =fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = westernmendb.objects.get(id=dataid).Image
            westernmendb.objects.filter(id=dataid).update(DressName=na, Code=co, Price=pr, Image=file)
            return redirect(displaymen)

def deletemen(request,dataid):
    data=westernmendb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaymen)


def accessori(request):
    return render(request,'Accessories.html')

def accessorydb(request):
    if request.method=="POST":
        na = request.POST.get('name')
        co = request.POST.get('code')
        pr = request.POST.get('price')
        img = request.FILES['image']

        obj = Accessoriesdb(AccessoriesName=na, Code=co, Price=pr, Image=img)
        obj.save()
        return redirect(westernpage)


def displayaccess(request):
    data=Accessoriesdb.objects.all()
    return render(request,'displayaccessories.html',{'data':data})

def editaccess(request,dataid):
    data=Accessoriesdb.objects.get(id=dataid)
    print(data)
    return render(request,'editaccess.html',{'data':data})

def updateaccess(request,dataid):
    if request.method=="POST":
        na = request.POST.get('name')
        co = request.POST.get('code')
        pr = request.POST.get('price')
        try:
            img=request.FILES['image']
            fs =FileSystemStorage()
            file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file =Accessoriesdb.objects.get(id=dataid).Image
            Accessoriesdb.objects.filter(id=dataid).update(AccessoriesName=na, Code=co, Price=pr, Image=file)
            return redirect(displayaccess)


def deleteaccess(request,dataid):
    data=Accessoriesdb.objects.filter(id=dataid)
    data.delete()
    return redirect(displayaccess)


def adminpage(request):
    return render(request,'admin.html')

def admindb(request):
    if request.method == "POST":
        na = request.POST.get('name')
        mb = request.POST.get('mob')
        em = request.POST.get('mail')
        img = request.FILES['image']
        un = request.POST.get('username')
        pd = request.POST.get('pwd')
        cp = request.POST.get('confpwd')
        obj =adminpagedb(Name=na,MobileNumber=mb,EmailID=em,Image=img,UserName=un,Password=pd,ConfirmPassword=cp)
        obj.save()
        return redirect(adminpage)

def displayadmin(request):
    data=adminpagedb.objects.all()
    return render(request,'displayadmin.html',{'data':data})

def editadmin(request,dataid):
    data=adminpagedb.objects.get(id=dataid)
    print(data)
    return render(request,'editadmin.html',{'data':data})

def updateadmin(request,dataid):
    if request.method=="POST":
        na = request.POST.get('name')
        mb = request.POST.get('mob')
        em = request.POST.get('mail')
        un = request.POST.get('username')
        pd = request.POST.get('pwd')
        cp = request.POST.get('confpwd')
        try:
            img = request.FILES['image']
            fs=FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = adminpagedb.objects.get(id=dataid).Image
            adminpagedb.objects.filter(id=dataid).update(Name=na,MobileNumber=mb,EmailID=em,Image=file,UserName=un,Password=pd,ConfirmPassword=cp)
            return redirect(displayadmin)
def deleteadmin(request,dataid):
    data=adminpagedb.objects.filter(id=dataid)
    data.delete()
    return redirect(displayadmin)


def addproduct(request):
    data =categorydb.objects.all()
    return render(request,'product.html', {'data':data})

def productpage(request):
    if request.method=='POST':
        cn = request.POST.get('category')
        pn = request.POST.get('name')
        pr = request.POST.get('price')
        de = request.POST.get('desc')
        img = request.FILES['image']
        obj =productdatabase (CategoryName=cn,ProductName=pn,Price=pr,Description=de,Image=img)
        obj.save()
    return redirect(addproduct)

def displayproduct(request):
    data=productdatabase.objects.all()
    return render(request,'Productdisplay.html',{'data':data})

def editproduct(request,dataid):
    data = productdatabase.objects.get(id=dataid)
    da = categorydb.objects.all()
    print(data)
    return render(request,'editproduct.html',{'data':data,'da':da})


def updateproduct(request, dataid):
    if request.method == "POST":
        cn = request.POST.get('category')
        pn = request.POST.get('name')
        pr = request.POST.get('price')
        de = request.POST.get('desc')

        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = productdatabase.objects.get(id=dataid).Image
            productdatabase.objects.filter(id=dataid).update(CategoryName=cn, ProductName=pn, Price=pr, Description=de, Image=file)
    return redirect(displayproduct)

def deleteproduct(request,dataid):
    data =productdatabase.objects.filter(id=dataid)
    data.delete()
    return redirect(displayproduct)


def Logindetails(request):
    return render(request,'loginpage.html')

def adminlogin(request):
    if request.method=="POST":
        username_r=request.POST.get('user')
        password_r=request.POST.get('password')

        if User.objects.filter(username__contains=username_r).exists():
            user = authenticate(username=username_r,password=password_r)
            if user is not None:
                login(request,user)
                request.session['user']=username_r
                request.session['password']=password_r
                return redirect(indexpage)
            else:
                return redirect(Logindetails)
        else:
            return redirect(Logindetails)

def displaycontactdb(request):
    data = Contactdb.objects.all()
    return render(request,'displaycontact.html',{'data':data})

def delcontact(request,dataid):
    data = Contactdb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaycontactdb)

def displayblogdb(request):
    data=Blogdb.objects.all()
    return render(request,'displayblog.html',{'data':data})

def delblog(request,dataid):
    data=Blogdb.objects.filter(id=dataid)
    data.delete()
    return redirect(displayblogdb)


