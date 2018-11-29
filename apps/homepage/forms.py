from django import forms
from django.forms import Textarea
from .models import Menu
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


]

class MenuForm(forms.ModelForm):

    item_name=forms.CharField(label="Item Name *")
    # item_description=forms.CharField(label="Item Description *")
    item_price=forms.CharField(label="Item Price *")
    item_category=forms.ChoiceField(label="Item Category *", widget=forms.Select, choices=(menu_categories))


    # image=forms.ImageField(required=False)

    class Meta:
        model = Menu
        fields = [
        "item_name",
        "item_price",
        "item_category",
        ]

class MenuImageForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = [
        "image",
        ]
