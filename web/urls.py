from . import views
from django.urls import path, re_path

# Create your tests here.

app_name = 'web'

urlpatterns = [
    path('', views.index, name="index"),
    path('product-category', views.product_category_view, name="product_category"),
    
    path('service/', views.service_view, name='service'),
    re_path(r'^service-view/(?P<pk>.*)/$', views.service_single_view, name='service_single'),
    re_path(r'^create-service/$', views.create_service_view, name='create_service'),
    re_path(r'^edit-service/(?P<pk>.*)/$', views.edit_service_view, name='edit_service'),
    re_path(r'^delete-service/(?P<pk>.*)/$', views.delete_service_view, name='delete_service'),
    
    
    path('career/', views.career_view, name='career'),
    re_path(r'^career-view/(?P<pk>.*)/$', views.career_single_view, name='career_single'),
    re_path(r'^create-career/$', views.create_career_view, name='create_career'),
    re_path(r'^edit-career/(?P<pk>.*)/$', views.edit_career_view, name='edit_career'),
    re_path(r'^delete-career/(?P<pk>.*)/$', views.delete_career_view, name='delete_career'),
    
    
    path('team-member/', views.team_members_view, name='team_member'),
    re_path(r'^team-member-view/(?P<pk>.*)/$', views.team_members_single_view, name='team_single'),
    re_path(r'^create-team-member/$', views.create_team_member_view, name='create_team_member'),
    re_path(r'^edit-team-member/(?P<pk>.*)/$', views.edit_team_member_view, name='edit_team_member'),
    re_path(r'^delete-team-member/(?P<pk>.*)/$', views.delete_team_member_view, name='delete_team_member'),
    
    
    path('about-us/', views.about_us_view, name='about_us'),
    re_path(r'^about-us-view/(?P<pk>.*)/$', views.about_us_single_view, name='about_us_single'),
    re_path(r'^create-about-us/$', views.create_about_us_view, name='create_about_us'),
    re_path(r'^edit-about-us/(?P<pk>.*)/$', views.edit_about_us_view, name='edit_about_us'),
    re_path(r'^delete-about-us/(?P<pk>.*)/$', views.delete_about_us_view, name='delete_about_us'),


    path('testimonial/', views.testimonial_view, name='testimonial'),
    re_path(r'^testimonial-view/(?P<pk>.*)/$', views.testimonial_single_view, name='testimonial_single'),
    re_path(r'^create-testimonial/$', views.create_testimonial_view, name='create_testimonial'),
    re_path(r'^edit-testimonial/(?P<pk>.*)/$', views.edit_testimonial_view, name='edit_testimonial'),
    re_path(r'^delete-testimonial/(?P<pk>.*)/$', views.delete_testimonial_view, name='delete_testimonial'),
    
    
    path('address/', views.address_view, name='address'),
    re_path(r'^address-view/(?P<pk>.*)/$', views.address_single_view, name='address_single'),
    re_path(r'^create-address/$', views.create_address_view, name='create_address'),
    re_path(r'^edit-address/(?P<pk>.*)/$', views.edit_address_view, name='edit_address'),
    re_path(r'^delete-address/(?P<pk>.*)/$', views.delete_address_view, name='delete_address'),
    
    
    path('connect/', views.connect_view, name='connect'),
    re_path(r'^create-connect/$', views.create_connect_view, name='create_connect'),
    re_path(r'^edit-connect/(?P<pk>.*)/$', views.edit_connect_view, name='edit_connect'),
    re_path(r'^delete-connect/(?P<pk>.*)/$', views.delete_connect_view, name='delete_connect'),
    
    path('description/', views.description_view, name='description'),
    re_path(r'^create-description/$', views.create_description_view, name='create_description'),
    re_path(r'^edit-description/(?P<pk>.*)/$', views.edit_description_view, name='edit_description'),

]