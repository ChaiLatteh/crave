# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime, date
import re, datetime, bcrypt
EMAIL_REGEX=re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

now = datetime.datetime.now()

# Create your models here.
class AdminManager(models.Manager):
    def login(self, data):
        errors=[]
        try:
            found_admin = Admin.objects.get(username=data['username'])
            if bcrypt.hashpw(data['password'].encode('utf-8'), found_admin.password.encode('utf-8')) != found_admin.password.encode('utf-8'):
                errors.append("Incorrect Password.")
        except:
            errors.append("Incorrect Username.")

        if len(errors)>0:
            return{
            'logged_admin':None,
            'errors_list':errors,
            }
        else:
            return{
        'logged_admin':found_admin,
        'errors_list':None,
        }

# class MenuManager(models.Manager):
    # def modify(self, data):
    #     errors=[]
    #     this_item=data['this_item']
    #
    #     if data['item_name']=="":
    #         errors.append("Please enter item name.")
    #     if data['item_price']=="":
    #         errors.append("Please enter item price.")
    #     if data['item_category']=="":
    #         errors.append("Please enter item category.")
    #
    #     if len(errors)>0:
    #         return{
    #         'item':None,
    #         'errors_list':errors,
    #         }
    #     else:
    #         this_item.item_name=data['item_name']
    #         this_item.item_price=data['item_price']
    #         this_item.item_category=data['item_category']
    #         this_item.save()
    #
    #         return{
    #         'item':this_item,
    #         'errors_list':None,
    #         }



class Admin(models.Model):
    username=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=AdminManager()

    def __str__(self):
        return self.username

class Menu(models.Model):
    # item_name=models.CharField(max_length=255)
    # item_price=models.CharField(max_length=255)
    # item_category=models.CharField(max_length=255)
    # item_description=models.CharField(max_length=255)
    image=models.ImageField(upload_to="menu_picture", null=True, blank=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    # objects=MenuManager()
