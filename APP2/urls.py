from django.urls import path
from APP2 import views
urlpatterns=[
    path('',views.Homepage,name='Homepage'),
    path('Aboutpage/', views.Aboutpage, name='Aboutpage'),
    path('Contactpage/', views.Contactpage, name='Contactpage'),
    path('Productdetails/',views.Productdetails,name='Productdetails'),
    path('displaycategory/<itemCatg>/',views.displaycategory,name='displaycategory'),
    path('displayproduct/<int:dataid>/',views.displayproduct,name='displayproduct'),
    path('loginadmin/',views.loginadmin,name='loginadmin'),
    path('signuppg/',views.signuppg,name='signuppg'),
    path('customersave/',views.customersave,name='customersave'),
    path('customerlogin/', views.customerlogin, name='customerlogin'),
    path('customerlogout/', views.customerlogout, name='customerlogout'),
    path('Blogpage/', views.Blogpage, name='Blogpage'),
    path('Contactdatabase/', views.Contactdatabase, name='Contactdatabase'),
    path('Blogdatabase/', views.Blogdatabase, name='Blogdatabase'),
    path('cartpage/',views.cartpage,name='cartpage'),
    path('cartdbfn/',views.cartdbfn,name='cartdbfn'),
    path('deleteitem/<int:dataid>/', views.deleteitem, name='deleteitem')






]