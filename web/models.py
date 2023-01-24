from django.db import models
from main.models import BaseModel
from versatileimagefield.fields import VersatileImageField
from main.variables import phone_regex

# Create your models here.

OFFICE_TYPE =(
    ("main_office","Main Office"),
    ("sub_office","Sub Office"),
)


class Service(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = VersatileImageField('Image', upload_to="web/service")

    class Meta:
        db_table = 'web_services'
        verbose_name = ('Services')
        verbose_name_plural = ('Services')
        ordering = ('auto_id',)

    def __str__(self):
        return str(self.title)
    

class Career(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    email = models.EmailField()

    class Meta:
        db_table = 'web_career'
        verbose_name = ('Career')
        verbose_name_plural = ('Career')
        ordering = ('auto_id',)

    def __str__(self):
        return str(self.title)
    

class TeamMember(BaseModel):
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    instagram_link = models.URLField()
    facebook_link = models.URLField()
    twitter_link = models.URLField()
    whatsapp_link = models.URLField()

    class Meta:
        db_table = 'web_team_member'
        verbose_name = ('Team Member')
        verbose_name_plural = ('Team Member')
        ordering = ('auto_id',)

    def __str__(self):
        return str(self.name)
    

class AboutUs(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = VersatileImageField('Image', upload_to="web/aboutus")

    class Meta:
        db_table = 'web_about_us'
        verbose_name = ('About Us')
        verbose_name_plural = ('About Us')
        ordering = ('auto_id',)

    def __str__(self):
        return str(self.title)
    

class Testimonial(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = VersatileImageField('Image', upload_to="web/testimonial")
    rating = models.PositiveIntegerField()

    class Meta:
        db_table = 'web_testimonial'
        verbose_name = ('Testimonial')
        verbose_name_plural = ('Testimonial')
        ordering = ('auto_id',)

    def __str__(self):
        return str(self.name)
    
    
class Address(BaseModel):
    phone = models.CharField(max_length=15 ,validators=[phone_regex],)
    email = models.EmailField()
    location = models.TextField()
    location_url = models.URLField()
    office_type = models.CharField(max_length=200,choices=OFFICE_TYPE)

    class Meta:
        db_table = 'web_address'
        verbose_name = ('Address')
        verbose_name_plural = ('Address')
        ordering = ('auto_id',)

    def __str__(self):
        return str(self.phone)
    
    
class Connect(BaseModel):
    instagram_link = models.URLField()
    facebook_link = models.URLField()
    twitter_link = models.URLField()
    linkedin_link = models.URLField()

    class Meta:
        db_table = 'web_connect'
        verbose_name = ('Connect')
        verbose_name_plural = ('Connect')
        ordering = ('auto_id',)

    def __str__(self):
        return str(self.instagram_link)
    

class Description(BaseModel):
    we_provides = models.TextField()
    our_services = models.TextField()
    careers = models.TextField()
    team_members = models.TextField()
    about_us = models.TextField()

    class Meta:
        db_table = 'web_description'
        verbose_name = ('Description')
        verbose_name_plural = ('Description')
        ordering = ('auto_id',)

    def __str__(self):
        return str(self.id)
    
    