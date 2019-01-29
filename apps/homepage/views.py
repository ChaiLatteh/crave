# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
import datetime, requests

from .models import Admin, MenuItem
from .forms import MenuItemForm, MenuImageForm

# Create your views here.
def home(request):
    return render(request, 'homepage/home.html')

def menu_images(request):
    return render(request, 'homepage/menu_images.html')

def menu(request):

    all_item_list=[]
    smoothie_list=[]
    special_smoothie_list=[]
    slush_list=[]
    milk_tea_list=[]
    jasmine_tea_list=[]
    special_drink_list=[]
    frappe_list=[]
    milkshake_list=[]
    waffle_list=[]
    milk_snow_list=[]
    acai_pitaya_list=[]
    cafe_list=[]
    hot_tea_list=[]
    taiyaki_list=[]
    ice_cream_list=[]

    for item in MenuItem.objects.all():
        all_item_list.append(item)

        if item.category=="smoothie":
            smoothie_list.append(item)
        if item.category=="special_smoothie":
            special_smoothie_list.append(item)
        if item.category=="slush":
            slush_list.append(item)
        if item.category=="milk_tea":
            milk_tea_list.append(item)
        if item.category=="jasmine_tea":
            jasmine_tea_list.append(item)
        if item.category=="special_drink":
            special_drink_list.append(item)
        if item.category=="frappe":
            frappe_list.append(item)
        if item.category=="milkshake":
            milkshake_list.append(item)
        if item.category=="waffle":
            waffle_list.append(item)
        if item.category=="milk_snow":
            milk_snow_list.append(item)
        if item.category=="acai_pitaya":
            acai_pitaya_list.append(item)
        if item.category=="cafe":
            cafe_list.append(item)
        if item.category=="hot_tea":
            hot_tea_list.append(item)
        if item.category=="taiyaki":
            taiyaki_list.append(item)
        if item.category=="ice_cream":
            ice_cream_list.append(item)

    data = {
    "all_item_list": all_item_list,

    "smoothie_list": smoothie_list,
    "special_smoothie_list": special_smoothie_list,
    "special_drink_list": special_drink_list,
    "slush_list": slush_list,
    "milk_tea_list": milk_tea_list,
    "jasmine_tea_list": jasmine_tea_list,
    "frappe_list": frappe_list,
    "milkshake_list": milkshake_list,
    "waffle_list": waffle_list,
    "milk_snow_list": milk_snow_list,
    "acai_pitaya_list": acai_pitaya_list,
    "cafe_list": cafe_list,
    "hot_tea_list": hot_tea_list,
    "ice_cream_list": ice_cream_list,
    "taiyaki_list": taiyaki_list,

    }

    return render(request, 'homepage/menu.html', data)

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
    "menu_item_list":MenuItem.objects.all(),
    }

    return render(request, 'homepage/admin/admin.html', data)

def closing_soon(request):
    return render(request, 'homepage/closing_soon.html')

def menu_add_image(request, item_id):
    if 'username' not in request.session:
        return redirect('/login')

    form = MenuImageForm()
    data={
    "form":form,
    "this_menu":MenuItem.objects.get(id=item_id),
    }
    return render(request, 'homepage/admin/menu_add_image.html', data)

def menu_add_image_process(request, item_id):
    if 'username' not in request.session:
        return redirect('/login')

    this_menu = MenuItem.objects.get(id=item_id)

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
            return redirect('/admin/menu/'+item_id+'/add_image')

    else:
        messages.add_message(request, messages.ERROR, "Something went wrong. Image has not been updated.")
        # return redirect('/admin/menu/'+item_id+'/add_image')
        return redirect('/')

def menu_add(request):
    if 'username' not in request.session:
        return redirect('/login')

    data={
    "form":MenuItemForm(),
    }
    return render(request, 'homepage/admin/menu_add.html', data)

def menu_add_process(request):
    if 'username' not in request.session:
        return redirect('/')

    if request.POST:
        form = MenuItemForm(request.POST, request.FILES)
        if form.is_valid():
            new_item = form.save(commit=False)

            new_item.save()
            messages.add_message(request, messages.SUCCESS, "Item has been added.")
            return redirect('/admin/menu/add')
        else:
            form = MenuItemForm()
            messages.add_message(request, messages.ERROR, "Please complete all required fields.")
            return redirect('/admin/menu/add')
    else:
        messages.add_message(request, messages.ERROR, "Something went wrong. Item has NOT been added.")
    return redirect('/admin/menu/add')

def menu_modify(request, item_id):
    data={
    "this_item":MenuItem.objects.get(id=item_id),
    }
    return render(request, 'homepage/admin/menu_modify.html', data)

def menu_modify_process(request, item_id):
    if 'username' not in request.session:
        return redirect('/')

    this_item=MenuItem.objects.get(id=item_id)

    data={
    'this_item':this_item,
    'category':request.POST['item_category'],
    'name':request.POST['item_name'],
    'price':request.POST['item_price'],
    'description':request.POST['item_description'],
    }

    item = MenuItem.objects.modify(data)

    if item['errors_list']:
        for error in item['errors_list']:
            messages.add_message(request, messages.ERROR, error)
            return redirect('/admin/menu/'+item_id+'/modify')
    else:
        messages.add_message(request, messages.SUCCESS, "Item has been modified.")
        return redirect('/admin')


def menu_delete_process(request, item_id):
    if 'username' not in request.session:
        return redirect('/')

    this_item = MenuItem.objects.get(id=item_id)
    this_item.delete()
    messages.add_message(request, messages.SUCCESS, "Item has been deleted.")
    return redirect('/admin')
