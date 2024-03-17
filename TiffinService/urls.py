"""TiffinService URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from TiffinApp.views import * 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name="index"),
    path('index/',index,name="index"),
    path('UserReg/',UserReg,name="UserReg"),
    path('UserRegAct/',UserRegAct,name="UserRegAct"),
    path('login/',login,name="login"),
    path('LoginAct/',LoginAct,name="LoginAct"),
    path('userview/',userview,name="userview"),
    path('staff/',staff,name="staff"),
    path('StaffAct/',StaffAct,name="StaffAct"),
    path('menu/',menu,name="menu"),
    path('MenuAct/',MenuAct,name="MenuAct"),
    path('UserReghome/',UserReghome,name="UserReghome"),
    path('UVMenu/',UVMenu,name="UVMenu"),
    path('adminhome/',adminhome,name="adminhome"),
    path('DeleteStaff/',DeleteStaff,name="DeleteStaff"),
    path('DeleteMenu/',DeleteMenu,name="DeleteMenu"),
    path('UpdateMenu/',UpdateMenu,name="UpdateMenu"),
    path('UpdateMenuAct/',UpdateMenuAct,name="UpdateMenuAct"),
    path('recipe/',recipe,name="recipe"),
    path('RecipeAct/',RecipeAct,name="RecipeAct"),
    path('UpdateRecipe/',UpdateRecipe,name="UpdateRecipe"),
    path('UpdateRecipeAct/',UpdateRecipeAct,name="UpdateRecipeAct"),
    path('DeleteRecipe/',DeleteRecipe,name="DeleteRecipe"),
    path('PreOrder/',PreOrder,name="PreOrder"),
    path('PreOrderAct/',PreOrderAct,name="PreOrderAct"),
    path('DeletePreOrder/',DeletePreOrder,name="DeletePreOrder"), 
    path('POview/',POview,name="POview"),
    path('AcceptPreOrder/',AcceptPreOrder,name="AcceptPreOrder"),
    path('RejectPreOrder/',RejectPreOrder,name="RejectPreOrder"),
    path('Order/',Order,name="Order"),
    path('OrderAct/',OrderAct,name="OrderAct"),
    path('DeleteOrder/',DeleteOrder,name="DeleteOrder"), 
    path('Oview/',Oview,name="Oview"),
    path('AcceptOrder/',AcceptOrder,name="AcceptOrder"), 
    path('RejectOrder/',RejectOrder,name="RejectOrder"),
    path('staffhome/',staffhome,name="staffhome"),
    path('SVMenu/',SVMenu,name="SVMenu"),
    path('SPview/',SPview,name="SPview"),
    path('SOview/',SOview,name="SOview"),
    path('PayPreOrder/',PayPreOrder,name="PayPreOrder"),
    path('canteenhome/',canteenhome,name="canteenhome"),
    path('canteen/',canteen,name="canteen"),
    path('canteenact/',canteenact,name="canteenact"),
    path('aviewcanteen/',aviewcanteen,name="aviewcanteen"),
    path('accept/',accept,name="accept"),
    path('reject/',reject,name="reject"),
    path('uvcanteen/',uvcanteen,name="uvcanteen"),
    path('day/',day,name="day"),
    path('dayact/',dayact,name="dayact"),
    path('Deleteday/',Deleteday,name="Deleteday"),
    path('viewmenu/',viewmenu,name="viewmenu"),
    # path('bookfood/',bookfood,name="bookfood"),
    path('corder/',corder,name="corder"),
    path('requestcn/',requestcn,name="requestcn"),
    path('requestact/',requestact,name="requestact"),
    path('uaccept/',uaccept,name="uaccept"),
    path('ureject/',ureject,name="ureject"),
    path('foodlist/',foodlist,name="foodlist"),
    path('editaddr/',editaddr,name="editaddr"),
    path('updateeditaddr/',updateeditaddr,name="updateeditaddr"),
    path('foodact/',foodact,name="foodact"),
    path('uorder/',uorder,name="uorder"),
    path('assign/',assign,name="assign"),
    path('staffviewassign/',staffviewassign,name="staffviewassign"),
    path('custvieworder/',custvieworder,name="custvieworder"),
    path('uvcanteenorder/',uvcanteenorder,name="uvcanteenorder"),
    path('status/',status,name="status"),
    path('reports/',reports,name="reports"),
    path('areports/',areports,name="areports"),
    path('dreports/',dreports,name="dreports"),
    path('preports/',preports,name="preports"),
    path('dsreports/',dsreports,name="dsreports"),
    path('feedback/',feedback,name="feedback"),
    path('feedact/',feedact,name="feedact"),
    path('aviewfeedback/',aviewfeedback,name="aviewfeedback"),
    path('payment/',payment,name="payment"),
    path('payact/',payact,name="payact"),
    path('compay/',compay,name="compay"),
    path('calamt/',calamt,name="calamt"),
    path('payact1/',payact1,name="payact1"),
    path('custmyorder/',custmyorder,name="custmyorder"),
    path('upayhis/',upayhis,name="upayhis"),
    path('userpayview/',userpayview,name="userpayview"),
]
