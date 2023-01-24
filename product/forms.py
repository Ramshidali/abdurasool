from unicodedata import category
from django import forms
from django.forms.widgets import TextInput,Textarea,Select,DateInput,CheckboxInput,FileInput

from product.models import Category, Product


class CategoryForm(forms.ModelForm):
        
    class Meta:
        model = Category
        fields = ['title','description_title','description','image']
            
        widgets = {
            'title': TextInput(attrs={'class': 'required form-control h-20','placeholder' : 'Enter Title'}),
            'description_title': TextInput(attrs={'class': 'required form-control h-20','placeholder' : 'Enter Description Title'}),
            'description': Textarea(attrs={'class': 'required form-control text-area','placeholder' : 'Enter Description'}),
            'image': FileInput(attrs={'class': 'form-control dropify'}), 
        }
        
    def clean_image(self):
        
        image_file = self.cleaned_data.get('image')
        if not (image_file.name.endswith(".jpg") or image_file.name.endswith(".png")):
            raise forms.ValidationError("Only .jpg or .png files are accepted")
        return image_file
    
    
    
class ProductForm(forms.ModelForm):
        
    class Meta:
        model = Product
        fields = ['category','name','color','image']
            
        widgets = {
            'category': Select(attrs={'class': 'select2 form-control mb-3 custom-select','placeholder' : 'Select Category'}),
            'name': TextInput(attrs={'class': 'required form-control h-20','placeholder' : 'Enter Name'}),
            'color': TextInput(attrs={'class': 'required form-control h-20','placeholder' : 'Enter Color'}),
            'image': FileInput(attrs={'class': 'form-control dropify'}), 
        }
        
    def clean_image(self):
        
        image_file = self.cleaned_data.get('image')
        if not (image_file.name.endswith(".jpg") or image_file.name.endswith(".png")):
            raise forms.ValidationError("Only .jpg or .png files are accepted")
        return image_file