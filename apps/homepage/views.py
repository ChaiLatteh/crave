# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from datetime import datetime, date

from .models import Admin, Menu
from .forms import MenuForm, MenuImageForm

# Create your views here.
def home(request):
    return render(request, 'homepage/home.html')

def menu(request):
    return render(request, 'homepage/menu.html')

def about_us(request):
    return render(request, 'homepage/about_us.html')

def contact_us(request):
    return render(request, 'homepage/contact_us.html')

def careers(request):
    return render(request, 'homepage/careers.html')


def login(request):
    return render(request, 'homepage/admin/login.html')

def login_process(request):
    data = {
    'username':request.POST['username'],
    'password':request.POST['password'],
    }
    admin = Admin.objects.login(data)
    if admin['errors_list']:
        for error in admin['errors_list']:
            messages.add_message(request, messages.ERROR, error)
            return redirect('/login')
    else:
        request.session['username']=admin['logged_admin'].username
        return redirect('/admin')

def logout(request):
    del request.session['username']
    messages.add_message(request, messages.SUCCESS, "Successfully Logged Out!")
    return redirect('/login')

def admin(request):
    if 'username' not in request.session:
        return redirect('/login')

    data={
    "menu_list":Menu.objects.all(),
    }

    return render(request, 'homepage/admin/admin.html', data)

def closing_soon(request):
    return render(request, 'homepage/closing_soon.html')

def menu_add_image(request, menu_id):
    if 'username' not in request.session:
        return redirect('/login')

    form = MenuImageForm()
    data={
    "form":form,
    "this_menu":Menu.objects.get(id=menu_id),
    }
    return render(request, 'homepage/admin/menu_add_image.html', data)

def menu_add_image_process(request, menu_id):
    if 'username' not in request.session:
        return redirect('/login')

    this_menu = Menu.objects.get(id=menu_id)

    if request.POST:
        form = MenuImageForm(request.POST, request.FILES, instance=this_menu)
        if form.is_valid():
            this_menu = form.save(commit=False)
            this_menu.save()
            messages.add_message(request, messages.SUCCESS, "Image has been added!")
            return redirect('/admin')
        else:
            form = MenuImageForm()
            messages.add_message(request, messages.ERROR, "Please select an image.")
            return redirect('/admin/menu/'+menu_id+'/add_image')

    else:
        messages.add_message(request, messages.ERROR, "Something went wrong. Image has not been updated.")
        return redirect('/admin/menu/'+menu_id+'/add_image')

# def menu_add(request):
#     if 'username' not in request.session:
#         return redirect('/login')
#
#     data={
#     "form":MenuForm(),
#     }
#     return render(request, 'homepage/admin/menu_add.html', data)
#
# def menu_add_process(request):
#     if 'username' not in request.session:
#         return redirect('/')
#
#     if request.POST:
#         form = MenuForm(request.POST, request.FILES)
#         if form.is_valid():
#             new_item = form.save(commit=False)
#
#             new_item.save()
#             messages.add_message(request, messages.SUCCESS, "Item has been added.")
#             return redirect('/admin/menu/add')
#         else:
#             form = MenuForm()
#             messages.add_message(request, messages.ERROR, "Please complete all required fields.")
#             return redirect('/admin/menu/add')
#     else:
#         messages.add_message(request, messages.ERROR, "Something went wrong. Item has NOT been added.")
#     return redirect('/admin/menu/add')
#
# def menu_modify(request, menu_id):
#     data={
#     "this_item":Menu.objects.get(id=menu_id),
#     }
#     return render(request, 'homepage/admin/menu_modify.html', data)
#
# def menu_modify_process(request, menu_id):
#     if 'username' not in request.session:
#         return redirect('/')
#
#     this_item=Menu.objects.get(id=menu_id)
#
#     data={
#     'this_item':this_item,
#     'item_name':request.POST['item_name'],
#     'item_price':request.POST['item_price'],
#     'item_category':request.POST['item_category'],
#     }
#
#     item = Menu.objects.modify(data)
#
#     if item['errors_list']:
#         for error in item['errors_list']:
#             messages.add_message(request, messages.ERROR, error)
#             return redirect('/admin/menu/'+menu_id+'/modify')
#     else:
#         messages.add_message(request, messages.SUCCESS, "Item has been modified.")
#         return redirect('/admin')
#
#
# def menu_delete_process(request, menu_id):
#     pass
