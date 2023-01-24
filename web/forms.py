from django import forms
from django.forms.widgets import TextInput,Textarea,Select,DateInput,CheckboxInput,FileInput

from web.models import AboutUs, Address, Career, Connect, Description, Service, TeamMember, Testimonial



class ServiceForm(forms.ModelForm):
        
    class Meta:
        model = Service
        fields = ['title','description','image']
            
        widgets = {
            'title': TextInput(attrs={'class': 'required form-control h-20','placeholder' : 'Enter Title'}),
            'description': Textarea(attrs={'class': 'required form-control h-20','placeholder' : 'Enter Title'}),
            'image': FileInput(attrs={'class': 'form-control dropify'}), 
        }
        
    def clean_image(self):
        
        image_file = self.cleaned_data.get('image')
        if not (image_file.name.endswith(".jpg") or image_file.name.endswith(".png")):
            raise forms.ValidationError("Only .jpg or .png files are accepted")
        return image_file
    
    
class CareerForm(forms.ModelForm):
        
    class Meta:
        model = Career
        fields = ['title','description','email']
            
        widgets = {
            'title': TextInput(attrs={'class': 'required form-control h-20','placeholder' : 'Enter Title'}),
            'description': Textarea(attrs={'class': 'required form-control h-20','placeholder' : 'Enter Title'}),
            'email': TextInput(attrs={'class': 'required form-control h-20','placeholder' : 'Enter Email'}),
        }
        
        
class TeamMembersForm(forms.ModelForm):
        
    class Meta:
        model = TeamMember
        fields = ['name','designation','instagram_link','facebook_link','twitter_link','whatsapp_link']
            
        widgets = {
            'name': TextInput(attrs={'class': 'required form-control h-20','placeholder' : 'Enter Title'}),
            'designation': TextInput(attrs={'class': 'required form-control h-20','placeholder' : 'Enter Designation'}),
            'instagram_link': TextInput(attrs={'class': 'required form-control h-20','placeholder' : 'Enter Instagram Link'}),
            'facebook_link': TextInput(attrs={'class': 'required form-control h-20','placeholder' : 'Enter Facebook Link'}),
            'twitter_link': TextInput(attrs={'class': 'required form-control h-20','placeholder' : 'Enter Twitter Link'}),
            'whatsapp_link': TextInput(attrs={'class': 'required form-control h-20','placeholder' : 'Enter Whatsapp Link'}),
        }
        
        
class AboutUsForm(forms.ModelForm):
        
    class Meta:
        model = AboutUs
        fields = ['title','description','image']
            
        widgets = {
            'title': TextInput(attrs={'class': 'required form-control h-20','placeholder' : 'Enter Title'}),
            'description': Textarea(attrs={'class': 'required form-control h-20','placeholder' : 'Enter Description'}),
            'image': FileInput(attrs={'class': 'form-control dropify'}), 
        }
        
    def clean_image(self):
        
        image_file = self.cleaned_data.get('image')
        if not (image_file.name.endswith(".jpg") or image_file.name.endswith(".png")):
            raise forms.ValidationError("Only .jpg or .png files are accepted")
        return image_file
    
    
    
class TestimonialForm(forms.ModelForm):
        
    class Meta:
        model = Testimonial
        fields = ['name','description','image','rating']
            
        widgets = {
            'name': TextInput(attrs={'class': 'required form-control h-20','placeholder' : 'Enter Name'}),
            'description': Textarea(attrs={'class': 'required form-control h-20','placeholder' : 'Enter Description'}),
            'rating': TextInput(attrs={'class': 'required form-control h-20','placeholder' : 'Enter rating'}),
            'image': FileInput(attrs={'class': 'form-control dropify'}), 
        }
        
    def clean_image(self):
        
        image_file = self.cleaned_data.get('image')
        if not (image_file.name.endswith(".jpg") or image_file.name.endswith(".png")):
            raise forms.ValidationError("Only .jpg or .png files are accepted")
        return image_file
    
    
class AddressForm(forms.ModelForm):
    
    class Meta:
        model = Address
        fields = ['phone','email','location','location_url','office_type']
            
        widgets = {
            'phone': TextInput(attrs={'class': 'required form-control h-20','placeholder' : 'Enter Phone'}),
            'email': TextInput(attrs={'class': 'required form-control h-20','placeholder' : 'Enter Email'}),
            'location': Textarea(attrs={'class': 'required form-control h-20','placeholder' : 'Enter Location'}),
            'location_url': TextInput(attrs={'class': 'required form-control h-20','placeholder' : 'Enter Location Url'}),
            'office_type': Select(attrs={'class': 'form-control selectpicker','placeholder' : 'office type'}),
        }
        
        
class ConnectForm(forms.ModelForm):
    
    class Meta:
        model = Connect
        fields = ['instagram_link','facebook_link','twitter_link','linkedin_link']
            
        widgets = {
            'instagram_link': TextInput(attrs={'class': 'required form-control h-20','placeholder' : 'Enter Instagram ID'}),
            'facebook_link': TextInput(attrs={'class': 'required form-control h-20','placeholder' : 'Enter Facebook ID'}),
            'twitter_link': TextInput(attrs={'class': 'required form-control h-20','placeholder' : 'Enter Twitter ID'}),
            'linkedin_link': TextInput(attrs={'class': 'required form-control h-20','placeholder' : 'Enter Linkedin ID'}),
        }
        
        
        
class DescriptionForm(forms.ModelForm):
    
    class Meta:
        model = Description
        fields = ['we_provides','our_services','careers','team_members','about_us']
            
        widgets = {
            'we_provides': Textarea(attrs={'class': 'required form-control h-20','placeholder' : 'Enter We Provided Description'}),
            'our_services': Textarea(attrs={'class': 'required form-control h-20','placeholder' : 'Enter Our Services Description'}),
            'careers': Textarea(attrs={'class': 'required form-control h-20','placeholder' : 'Enter Careers Description'}),
            'team_members': Textarea(attrs={'class': 'required form-control h-20','placeholder' : 'Enter Team members Description'}),
            'about_us': Textarea(attrs={'class': 'required form-control h-20','placeholder' : 'Enter About Us Description'}),
        }