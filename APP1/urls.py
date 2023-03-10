from django.urls import path
from APP1 import views
urlpatterns = [
    path('indexpage/',views.indexpage,name='indexpage'),
    path('categorypage/' ,views.categorypage ,name='categorypage'),
    path('categorypagedb/' ,views.categorypagedb ,name='categorypagedb'),
    path('displaycategory/' ,views.displaycategory ,name='displaycategory'),
    path('editcategorypage/<int:dataid>/' ,views.editcategorypage ,name='editcategorypage'),
    path('updatecategorypage/<int:dataid>/' ,views.updatecategorypage ,name='updatecategorypage'),
    path('deletecategory/<int:dataid>/' ,views.deletecategory ,name='deletecategory'),
    path('adminpage/',views.adminpage,name='adminpage'),
    path('admindb/', views.admindb, name='admindb'),
    path('displayadmin/', views.displayadmin, name='displayadmin'),
    path('editadmin/<int:dataid>/', views.editadmin, name='editadmin'),
    path('updateadmin/<int:dataid>/', views.updateadmin, name='updateadmin'),
    path('deleteadmin/<int:dataid>/', views.deleteadmin, name='deleteadmin'),
    path('addproduct/',views.addproduct,name='addproduct'),
    path('productpage/',views.productpage,name='productpage'),
    path('displayproduct/',views.displayproduct,name='displayproduct'),
    path('editproduct/<int:dataid>/',views.editproduct,name='editproduct'),
    path('updateproduct/<int:dataid>/',views.updateproduct,name='updateproduct'),
    path('deleteproduct/<int:dataid>/',views.deleteproduct,name='deleteproduct'),
    path('Logindetails/',views.Logindetails,name='Logindetails'),
    path('adminlogin/', views.adminlogin, name='adminlogin'),
    path('displaycontactdb/', views.displaycontactdb, name='displaycontactdb'),
    path('delcontact/<int:dataid>/', views.delcontact, name='delcontact'),
    path('displayblogdb/', views.displayblogdb, name='displayblogdb'),
    path('delblog/<int:dataid>/', views.delblog, name='delblog')

]