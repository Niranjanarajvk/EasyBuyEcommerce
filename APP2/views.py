from django.shortcuts import render,redirect
from APP1.models import categorydb,productdatabase,Contactdb,Blogdb
from APP2.models import CustomerDetails,cartdb
from django.contrib import messages

# Create your views here.
def Homepage(request):
    data=categorydb.objects.all()
    da=cartdb.objects.all()
    products=productdatabase.objects.all()
    return render(request,'webindex.html',{'data':data ,'products':products,'da':da})


def Aboutpage(request):
    data=categorydb.objects.all()
    da = cartdb.objects.all()
    return render(request,'About.html',{'data':data, 'da':da})

def Contactpage(request):
    data=categorydb.objects.all()
    da = cartdb.objects.all()
    return render(request,'Contact.html',{'data':data,'da':da})

def Contactdatabase(request):
    if request.method=="POST":
        em=request.POST.get('email')
        ms=request.POST.get('msg')
        obj=Contactdb(EmailID=em,Message=ms)
        obj.save()
    return redirect(Contactpage)

def Productdetails(request):
    data1 = productdatabase.objects.all()
    da = cartdb.objects.all()
    data=categorydb.objects.all()
    return render(request, 'App2Product.html', {'data1': data1,'data':data,'da':da})


def displaycategory(request,itemCatg):
    data=categorydb.objects.all()
    da=cartdb.objects.all()
    print("===itemCatg===",itemCatg)
    catg=itemCatg.upper()
    products=productdatabase.objects.filter(CategoryName=itemCatg)
    context = {
        'products':products,
        'catg':catg,
        'data':data,
        'da':da

    }
    return render(request,'Categorydisplay.html',context)



def displayproduct(request,dataid):
    data1=categorydb.objects.all()
    da = cartdb.objects.all()
    data=productdatabase.objects.get(id=dataid)
    context2 ={
        'data': data,
        'data1': data1,
        'da': da

    }
    return render(request,'Productcontent.html',context2)

def loginadmin(request):
    data=categorydb.objects.all()
    da = cartdb.objects.all()
    return render(request,'LoginReg.html',{'data':data,'da': da })
def signuppg(request):
    data = categorydb.objects.all()
    da = cartdb.objects.all()
    return render(request,'Registration.html',{'data':data, 'da':da})
def customersave(request):
    if request.method=="POST":
        un=request.POST.get('username')
        em=request.POST.get('email')
        pw=request.POST.get('password')
        cp=request.POST.get('confirmpassword')
        if pw==cp:
            obj = CustomerDetails(username=un,email=em,password=pw,confirmpassword=cp)
            obj.save()
            messages.success(request,"User Register Successfully")
            return redirect(loginadmin)
        else:
            messages.warning(request, "Sorry.... Invalid Username Or Password")
            return redirect(signuppg)
    return render(request, 'Registration.html',{'msg': "sorry.... password not matched"})

def customerlogin(request):
    if request.method=='POST':
        username_r = request.POST.get("username")
        password_r = request.POST.get("password")
        if CustomerDetails.objects.filter(username=username_r,password=password_r).exists():
            request.session['username'] = username_r
            request.session['password'] = password_r

            return redirect(Homepage)
        else:
            messages.warning(request,"sorry.... invalid username or password")
    return render(request, 'LoginReg.html')

def customerlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(Homepage)


def Blogpage(request):
    data=categorydb.objects.all()
    da = cartdb.objects.all()
    return render(request,'Blog.html',{'data':data,'da':da})

def Blogdatabase(request):
    if request.method=="POST":
        cm=request.POST.get('cmt')
        na = request.POST.get('name')
        em=request.POST.get('email')
        wb=request.POST.get('web')
        obj=Blogdb(Comment=cm,Name=na,EmailID=em,Website=wb)
        obj.save()
        return redirect(Blogpage)

def cartpage(request):
    data=categorydb.objects.all()
    da=cartdb.objects.all()
    return render(request,'cart.html',{'data':data ,'da':da})

def cartdbfn(request):
    if request.method=='POST':
        pn = request.POST.get('name')
        pr = request.POST.get('price')
        de = request.POST.get('desc')
        qn = request.POST.get('quantity')
        tp = request.POST.get('totalprice')
        obj =cartdb(ProductName=pn,Price=pr,Description=de,Quantity=qn,Totalprice=tp)
        obj.save()
    return redirect(cartpage)



def deleteitem(request,dataid):
    data=cartdb.objects.filter(id=dataid)
    data.delete()
    return redirect(cartpage)
