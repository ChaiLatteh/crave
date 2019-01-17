from django import forms
from django.forms import Textarea
from .models import MenuItem
import datetime

menu_categories=[
('', 'Select'),
('smoothie', 'Smoothie'),
('special_smoothie', 'Special Smoothie'),
('slush', 'Slush'),
('milkshake', 'Milkshake'),
('milk_tea', 'Milk Tea'),
('jasmine_tea', 'Jasmine Tea'),
('special_drink', 'Special Drink'),
('topping', 'Topping'),
('foam', 'Foam'),
('waffle', 'Waffle'),
('snow', 'Snow'),
('acai_pitaya', 'Acai & Pitaya'),
('coffee', 'Coffee'),
('hot_tea', 'Hot Tea'),
('icecream', 'Ice Cream'),
('icecream_cone', 'Ice Cream Cone'),
('taiyaki', 'Taiyaki'),


]

class MenuItemForm(forms.ModelForm):

    name=forms.CharField(label="Item Name *")
    description=forms.CharField(label="Item Description *")
    price=forms.CharField(label="Item Price *")
    category=forms.ChoiceField(label="Item Category *", widget=forms.Select, choices=(menu_categories))


    # image=forms.ImageField(required=False)

    class Meta:
        model = MenuItem
        fields = [
        "name",
        "price",
        "description",
        "category",
        ]

class MenuImageForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = [
        "image",
        ]
