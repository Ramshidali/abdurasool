import datetime
from email import message
import json
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.urls import reverse

from main.decorators import role_required
from main.functions import generate_form_errors, get_auto_id, paginate
from product.models import Category, Product
from web.forms import AboutUsForm, AddressForm, CareerForm, ConnectForm, DescriptionForm, ServiceForm, TeamMembersForm, TestimonialForm
from web.models import AboutUs, Address, Career, Connect, Description, Service, TeamMember, Testimonial

# Create your views here.



@login_required
@role_required(['superadmin'])
def service_single_view(request,pk):
    """
    service sigle view
    :param request:
    :return: service list view
    """
    instance = Service.objects.get(pk=pk,is_deleted=False)

    context = {
        'instance': instance,
        'page_name' : 'Our Service',
        'page_title' : 'Our Service',
        'active_page_name' : 'Service single view',
    }

    return render(request, 'admin_panel/product/single_view.html', context)


@login_required
@role_required(['superadmin'])
def service_view(request):
    """
    service listings
    :param request:
    :return: service list view
    """
    instances = Service.objects.filter(is_deleted=False).order_by("-id")
    
    filter_data = {}
    query = request.GET.get("q")
    
    if query:

        instances = instances.filter(
            Q(auto_id__icontains=query) |
            Q(name__icontains=query) 
        )
        title = "Service - %s" % query
        filter_data['q'] = query
    

    context = {
        'instances': instances,
        'page_name' : 'Our Services',
        'page_title' : 'Our Services',
        'filter_data' :filter_data,
    }

    return render(request, 'admin_panel/product/service_list.html', context)


@login_required
@role_required(['superadmin'])
def create_service_view(request):
    """
    create operation of services
    :param request:
    :param pk:
    :return:
    """
    if request.method == 'POST':
        # if instance go to edit
        form = ServiceForm(request.POST,request.FILES)
            
        if form.is_valid():
            data = form.save(commit=False)
            data.auto_id = get_auto_id(Service)
            data.creator = request.user
            data.date_updated = datetime.datetime.today()
            data.updater = request.user
            data.save()

            response_data = {
                "status": "true",
                "title": "Successfully Created",
                "message": "Service created successfully.",
                'redirect': 'true',
                "redirect_url": reverse('web:service')
            }
    
        else:
            message =generate_form_errors(form , formset=False)
            response_data = {
                "status": "false",
                "title": "Failed",
                "message": message,
            }

        return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    
    else:
        
        form = ServiceForm()

        context = {
            'form': form,
            'page_name' : 'Create Service',
            'page_title' : 'Create Service',
            'url' : reverse('web:create_service'),
        }

        return render(request, 'admin_panel/create/create.html',context)

    
@login_required
@role_required(['superadmin'])
def edit_service_view(request,pk):
    """
    edit operation of service
    :param request:
    :param pk:
    :return:
    """
    instance = get_object_or_404(Service, pk=pk)
        
    message = ''
    if request.method == 'POST':
        form = ServiceForm(request.POST,request.FILES,instance=instance)
        
        if form.is_valid():
            
            #update product
            data = form.save(commit=False)
            data.date_updated = datetime.datetime.today()
            data.updater = request.user
            data.save()
                    
            response_data = {
                "status": "true",
                "title": "Successfully Updated",
                "message": "Service Update successfully.",
                'redirect': 'true',
                "redirect_url": reverse('web:service')
            }
    
        else:
            message = generate_form_errors(form ,formset=False)
            
            
            response_data = {
                "status": "false",
                "title": "Failed",
                "message": message
            }

        return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    
    else:
        
        form = ServiceForm(instance=instance)

        context = {
            'form': form,
            'page_name' : 'Update Service',
            'page_title' : 'Update Service',
            'is_need_select2' : True,
            'url' : reverse('web:service'),
        }

        return render(request, 'admin_panel/create/create.html',context)


@login_required
@role_required(['superadmin'])
def delete_service_view(request, pk):
    """
    service deletion, it only mark as is deleted field to true
    :param request:
    :param pk:
    :return:
    """
    Service.objects.filter(pk=pk).update(is_deleted=True)

    response_data = {
        "status": "true",
        "title": "Successfully Deleted",
        "message": "Service Successfully Deleted.",
        "redirect": "true",
        "redirect_url": reverse('web:service')
    }

    return HttpResponse(json.dumps(response_data), content_type='application/javascript')



@login_required
@role_required(['superadmin'])
def career_single_view(request,pk):
    """
    career sigle view
    :param request:
    :return: career list view
    """
    instance = Career.objects.get(pk=pk,is_deleted=False)

    context = {
        'instance': instance,
        'page_name' : 'Careers',
        'page_title' : 'Careers',
        'active_page_name' : 'Career single view',
    }

    return render(request, 'admin_panel/product/career_single.html', context)


@login_required
@role_required(['superadmin'])
def career_view(request):
    """
    careers listings
    :param request:
    :return: service list view
    """
    instances = Career.objects.filter(is_deleted=False).order_by("-id")
    
    filter_data = {}
    query = request.GET.get("q")
    
    if query:

        instances = instances.filter(
            Q(auto_id__icontains=query) |
            Q(name__icontains=query) 
        )
        title = "Career - %s" % query
        filter_data['q'] = query
    

    context = {
        'instances': instances,
        'page_name' : 'Careers',
        'page_title' : 'Careers',
        'filter_data' :filter_data,
    }

    return render(request, 'admin_panel/product/careers_list.html', context)


@login_required
@role_required(['superadmin'])
def create_career_view(request):
    """
    create operation of career
    :param request:
    :param pk:
    :return:
    """
    if request.method == 'POST':
        # if instance go to edit
        form = CareerForm(request.POST,request.FILES)
            
        if form.is_valid():
            data = form.save(commit=False)
            data.auto_id = get_auto_id(Career)
            data.creator = request.user
            data.date_updated = datetime.datetime.today()
            data.updater = request.user
            data.save()

            response_data = {
                "status": "true",
                "title": "Successfully Created",
                "message": "Career created successfully.",
                'redirect': 'true',
                "redirect_url": reverse('web:career')
            }
    
        else:
            message =generate_form_errors(form , formset=False)
            response_data = {
                "status": "false",
                "title": "Failed",
                "message": message,
            }

        return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    
    else:
        
        form = CareerForm()

        context = {
            'form': form,
            'page_name' : 'Create Career',
            'page_title' : 'Create Career',
            'url' : reverse('web:create_career'),
        }

        return render(request, 'admin_panel/create/create.html',context)

    
@login_required
@role_required(['superadmin'])
def edit_career_view(request,pk):
    """
    edit operation of career
    :param request:
    :param pk:
    :return:
    """
    instance = get_object_or_404(Career, pk=pk)
        
    message = ''
    if request.method == 'POST':
        form = CareerForm(request.POST,request.FILES,instance=instance)
        
        if form.is_valid():
            
            #update product
            data = form.save(commit=False)
            data.date_updated = datetime.datetime.today()
            data.updater = request.user
            data.save()
                    
            response_data = {
                "status": "true",
                "title": "Successfully Updated",
                "message": "Career Update successfully.",
                'redirect': 'true',
                "redirect_url": reverse('web:career')
            }
    
        else:
            message = generate_form_errors(form ,formset=False)
            
            
            response_data = {
                "status": "false",
                "title": "Failed",
                "message": message
            }

        return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    
    else:
        
        form = CareerForm(instance=instance)

        context = {
            'form': form,
            'page_name' : 'Update Career',
            'page_title' : 'Update Career',
            'is_need_select2' : True,
            'url' : reverse('web:career'),
        }

        return render(request, 'admin_panel/create/create.html',context)


@login_required
@role_required(['superadmin'])
def delete_career_view(request, pk):
    """
    career deletion, it only mark as is deleted field to true
    :param request:
    :param pk:
    :return:
    """
    Career.objects.filter(pk=pk).update(is_deleted=True)

    response_data = {
        "status": "true",
        "title": "Successfully Deleted",
        "message": "Career Successfully Deleted.",
        "redirect": "true",
        "redirect_url": reverse('web:career')
    }

    return HttpResponse(json.dumps(response_data), content_type='application/javascript')



@login_required
@role_required(['superadmin'])
def team_members_single_view(request,pk):
    """
    team_members sigle view
    :param request:
    :return: team members list view
    """
    instance = TeamMember.objects.get(pk=pk,is_deleted=False)

    context = {
        'instance': instance,
        'page_name' : 'Team Members',
        'page_title' : 'Team Members',
        'active_page_name' : 'Team Member single view',
    }

    return render(request, 'admin_panel/product/team_member_single.html', context)


@login_required
@role_required(['superadmin'])
def team_members_view(request):
    """
    team members listings
    :param request:
    :return: team members list view
    """
    instances = TeamMember.objects.filter(is_deleted=False).order_by("-id")
    
    filter_data = {}
    query = request.GET.get("q")
    
    if query:

        instances = instances.filter(
            Q(auto_id__icontains=query) |
            Q(name__icontains=query) 
        )
        title = "Team Member - %s" % query
        filter_data['q'] = query
    

    context = {
        'instances': instances,
        'page_name' : 'Team Members',
        'page_title' : 'Team Members',
        'filter_data' :filter_data,
    }

    return render(request, 'admin_panel/product/team_members_list.html', context)


@login_required
@role_required(['superadmin'])
def create_team_member_view(request):
    """
    create operation of team member
    :param request:
    :param pk:
    :return:
    """
    if request.method == 'POST':
        # if instance go to edit
        form = TeamMembersForm(request.POST,request.FILES)
            
        if form.is_valid():
            data = form.save(commit=False)
            data.auto_id = get_auto_id(TeamMember)
            data.creator = request.user
            data.date_updated = datetime.datetime.today()
            data.updater = request.user
            data.save()

            response_data = {
                "status": "true",
                "title": "Successfully Created",
                "message": "Team Member created successfully.",
                'redirect': 'true',
                "redirect_url": reverse('web:team_member')
            }
    
        else:
            message =generate_form_errors(form , formset=False)
            response_data = {
                "status": "false",
                "title": "Failed",
                "message": message,
            }

        return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    
    else:
        
        form = TeamMembersForm()

        context = {
            'form': form,
            'page_name' : 'Create Team Member',
            'page_title' : 'Create Team Member',
            'url' : reverse('web:create_team_member'),
        }

        return render(request, 'admin_panel/create/create.html',context)

    
@login_required
@role_required(['superadmin'])
def edit_team_member_view(request,pk):
    """
    edit operation of team member
    :param request:
    :param pk:
    :return:
    """
    instance = get_object_or_404(TeamMember, pk=pk)
        
    message = ''
    if request.method == 'POST':
        form = TeamMembersForm(request.POST,instance=instance)
        
        if form.is_valid():
            
            #update product
            data = form.save(commit=False)
            data.date_updated = datetime.datetime.today()
            data.updater = request.user
            data.save()
                    
            response_data = {
                "status": "true",
                "title": "Successfully Updated",
                "message": "Team Member Update successfully.",
                'redirect': 'true',
                "redirect_url": reverse('web:team_member')
            }
    
        else:
            message = generate_form_errors(form ,formset=False)
            
            
            response_data = {
                "status": "false",
                "title": "Failed",
                "message": message
            }

        return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    
    else:
        
        form = TeamMembersForm(instance=instance)

        context = {
            'form': form,
            'page_name' : 'Update Team Member',
            'page_title' : 'Update Team Member',
            'is_need_select2' : True,
            'url' : reverse('web:team_member'),
        }

        return render(request, 'admin_panel/create/create.html',context)


@login_required
@role_required(['superadmin'])
def delete_team_member_view(request, pk):
    """
    team member deletion, it only mark as is deleted field to true
    :param request:
    :param pk:
    :return:
    """
    TeamMember.objects.filter(pk=pk).update(is_deleted=True)

    response_data = {
        "status": "true",
        "title": "Successfully Deleted",
        "message": "Team Member Successfully Deleted.",
        "redirect": "true",
        "redirect_url": reverse('web:team_member')
    }

    return HttpResponse(json.dumps(response_data), content_type='application/javascript')




@login_required
@role_required(['superadmin'])
def about_us_single_view(request,pk):
    """
    about us sigle view
    :param request:
    :return: about us list view
    """
    instance = AboutUs.objects.get(pk=pk,is_deleted=False)

    context = {
        'instance': instance,
        'page_name' : 'About Us',
        'page_title' : 'About Us',
        'active_page_name' : 'About Us single view',
    }

    return render(request, 'admin_panel/product/about_us_single.html', context)


@login_required
@role_required(['superadmin'])
def about_us_view(request):
    """
    about us listings
    :param request:
    :return: about us list view
    """
    instances = AboutUs.objects.filter(is_deleted=False).order_by("-id")
    
    filter_data = {}
    query = request.GET.get("q")
    
    if query:

        instances = instances.filter(
            Q(auto_id__icontains=query) |
            Q(name__icontains=query) 
        )
        title = "About Us - %s" % query
        filter_data['q'] = query
    

    context = {
        'instances': instances,
        'page_name' : 'About Us',
        'page_title' : 'About Us',
        'filter_data' :filter_data,
    }

    return render(request, 'admin_panel/product/about_us_list.html', context)


@login_required
@role_required(['superadmin'])
def create_about_us_view(request):
    """
    create operation of about us
    :param request:
    :param pk:
    :return:
    """
    if request.method == 'POST':
        # if instance go to edit
        form = AboutUsForm(request.POST,request.FILES,request.FILES)
            
        if form.is_valid():
            data = form.save(commit=False)
            data.auto_id = get_auto_id(AboutUs)
            data.creator = request.user
            data.date_updated = datetime.datetime.today()
            data.updater = request.user
            data.save()

            response_data = {
                "status": "true",
                "title": "Successfully Created",
                "message": "About Us created successfully.",
                'redirect': 'true',
                "redirect_url": reverse('web:about_us')
            }
    
        else:
            message =generate_form_errors(form , formset=False)
            response_data = {
                "status": "false",
                "title": "Failed",
                "message": message,
            }

        return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    
    else:
        
        form = AboutUsForm()

        context = {
            'form': form,
            'page_name' : 'Create About Us',
            'page_title' : 'Create About Us',
            'url' : reverse('web:create_about_us'),
        }

        return render(request, 'admin_panel/create/create.html',context)

    
@login_required
@role_required(['superadmin'])
def edit_about_us_view(request,pk):
    """
    edit operation of about us
    :param request:
    :param pk:
    :return:
    """
    instance = get_object_or_404(AboutUs, pk=pk)
        
    message = ''
    if request.method == 'POST':
        form = AboutUsForm(request.POST,request.FILES,instance=instance)
        
        if form.is_valid():
            
            #update product
            data = form.save(commit=False)
            data.date_updated = datetime.datetime.today()
            data.updater = request.user
            data.save()
                    
            response_data = {
                "status": "true",
                "title": "Successfully Updated",
                "message": "About Us Update successfully.",
                'redirect': 'true',
                "redirect_url": reverse('web:about_us')
            }
    
        else:
            message = generate_form_errors(form ,formset=False)
            
            
            response_data = {
                "status": "false",
                "title": "Failed",
                "message": message
            }

        return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    
    else:
        
        form = AboutUsForm(instance=instance)

        context = {
            'form': form,
            'page_name' : 'Update About Us',
            'page_title' : 'Update About Us',
            'is_need_select2' : True,
            'url' : reverse('web:about_us'),
        }

        return render(request, 'admin_panel/create/create.html',context)


@login_required
@role_required(['superadmin'])
def delete_about_us_view(request, pk):
    """
    about us deletion, it only mark as is deleted field to true
    :param request:
    :param pk:
    :return:
    """
    AboutUs.objects.filter(pk=pk).update(is_deleted=True)

    response_data = {
        "status": "true",
        "title": "Successfully Deleted",
        "message": "About Us Successfully Deleted.",
        "redirect": "true",
        "redirect_url": reverse('web:about_us')
    }

    return HttpResponse(json.dumps(response_data), content_type='application/javascript')




@login_required
@role_required(['superadmin'])
def testimonial_single_view(request,pk):
    """
    testimonial sigle view
    :param request:
    :return: about us list view
    """
    instance = Testimonial.objects.get(pk=pk,is_deleted=False)

    context = {
        'instance': instance,
        'page_name' : 'Testimonial',
        'page_title' : 'Testimonial',
        'active_page_name' : 'Testimonial single view',
    }

    return render(request, 'admin_panel/product/testimonial_single.html', context)


@login_required
@role_required(['superadmin'])
def testimonial_view(request):
    """
    testimonial listings
    :param request:
    :return: testimonial list view
    """
    instances = Testimonial.objects.filter(is_deleted=False).order_by("-id")
    
    filter_data = {}
    query = request.GET.get("q")
    
    if query:

        instances = instances.filter(
            Q(auto_id__icontains=query) |
            Q(name__icontains=query) 
        )
        title = "Testimonial - %s" % query
        filter_data['q'] = query
    

    context = {
        'instances': instances,
        'page_name' : 'Testimonial',
        'page_title' : 'Testimonial',
        'filter_data' :filter_data,
    }

    return render(request, 'admin_panel/product/testimonial_list.html', context)


@login_required
@role_required(['superadmin'])
def create_testimonial_view(request):
    """
    create operation of Testimonial
    :param request:
    :param pk:
    :return:
    """
    if request.method == 'POST':
        # if instance go to edit
        form = TestimonialForm(request.POST,request.FILES,request.FILES)
            
        if form.is_valid():
            data = form.save(commit=False)
            data.auto_id = get_auto_id(Testimonial)
            data.creator = request.user
            data.date_updated = datetime.datetime.today()
            data.updater = request.user
            data.save()

            response_data = {
                "status": "true",
                "title": "Successfully Created",
                "message": "Testimonial created successfully.",
                'redirect': 'true',
                "redirect_url": reverse('web:testimonial')
            }
    
        else:
            message =generate_form_errors(form , formset=False)
            response_data = {
                "status": "false",
                "title": "Failed",
                "message": message,
            }

        return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    
    else:
        
        form = TestimonialForm()

        context = {
            'form': form,
            'page_name' : 'Create Testimonial',
            'page_title' : 'Create Testimonial',
            'url' : reverse('web:create_testimonial'),
        }

        return render(request, 'admin_panel/create/create.html',context)

    
@login_required
@role_required(['superadmin'])
def edit_testimonial_view(request,pk):
    """
    edit operation of Testimonial
    :param request:
    :param pk:
    :return:
    """
    instance = get_object_or_404(Testimonial, pk=pk)
        
    message = ''
    if request.method == 'POST':
        form = TestimonialForm(request.POST,request.FILES,instance=instance)
        
        if form.is_valid():
            
            #update product
            data = form.save(commit=False)
            data.date_updated = datetime.datetime.today()
            data.updater = request.user
            data.save()
                    
            response_data = {
                "status": "true",
                "title": "Successfully Updated",
                "message": "Testimonial Update successfully.",
                'redirect': 'true',
                "redirect_url": reverse('web:testimonial')
            }
    
        else:
            message = generate_form_errors(form ,formset=False)
            
            
            response_data = {
                "status": "false",
                "title": "Failed",
                "message": message
            }

        return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    
    else:
        
        form = TestimonialForm(instance=instance)

        context = {
            'form': form,
            'page_name' : 'Update Testimonial',
            'page_title' : 'Update Testimonial',
            'is_need_select2' : True,
            'url' : reverse('web:testimonial'),
        }

        return render(request, 'admin_panel/create/create.html',context)


@login_required
@role_required(['superadmin'])
def delete_testimonial_view(request, pk):
    """
    Testimonial deletion, it only mark as is deleted field to true
    :param request:
    :param pk:
    :return:
    """
    Testimonial.objects.filter(pk=pk).update(is_deleted=True)

    response_data = {
        "status": "true",
        "title": "Successfully Deleted",
        "message": "Testimonial Successfully Deleted.",
        "redirect": "true",
        "redirect_url": reverse('web:testimonial')
    }

    return HttpResponse(json.dumps(response_data), content_type='application/javascript')



@login_required
@role_required(['superadmin'])
def address_single_view(request,pk):
    """
    Address sigle view
    :param request:
    :return: about us list view
    """
    instance = Address.objects.get(pk=pk,is_deleted=False)

    context = {
        'instance': instance,
        'page_name' : 'Address',
        'page_title' : 'Address',
        'active_page_name' : 'Address single view',
    }

    return render(request, 'admin_panel/product/address_single.html', context)


@login_required
@role_required(['superadmin'])
def address_view(request):
    """
    Address listings
    :param request:
    :return: Address list view
    """
    instances = Address.objects.filter(is_deleted=False).order_by("-id")
    
    filter_data = {}
    query = request.GET.get("q")
    
    if query:

        instances = instances.filter(
            Q(auto_id__icontains=query) |
            Q(name__icontains=query) 
        )
        title = "Address - %s" % query
        filter_data['q'] = query
    

    context = {
        'instances': instances,
        'page_name' : 'Address',
        'page_title' : 'Address',
        'filter_data' :filter_data,
    }

    return render(request, 'admin_panel/product/address_list.html', context)


@login_required
@role_required(['superadmin'])
def create_address_view(request):
    """
    create operation of Address
    :param request:
    :param pk:
    :return:
    """
    if request.method == 'POST':
        # if instance go to edit
        form = AddressForm(request.POST,request.FILES,request.FILES)
            
        if form.is_valid():
            data = form.save(commit=False)
            data.auto_id = get_auto_id(Address)
            data.creator = request.user
            data.date_updated = datetime.datetime.today()
            data.updater = request.user
            data.save()

            response_data = {
                "status": "true",
                "title": "Successfully Created",
                "message": "Address created successfully.",
                'redirect': 'true',
                "redirect_url": reverse('web:address')
            }
    
        else:
            message =generate_form_errors(form , formset=False)
            response_data = {
                "status": "false",
                "title": "Failed",
                "message": message,
            }

        return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    
    else:
        
        form = AddressForm()

        context = {
            'form': form,
            'page_name' : 'Create Address',
            'page_title' : 'Create Address',
            'url' : reverse('web:create_address'),
        }

        return render(request, 'admin_panel/create/create.html',context)

    
@login_required
@role_required(['superadmin'])
def edit_address_view(request,pk):
    """
    edit operation of Address
    :param request:
    :param pk:
    :return:
    """
    instance = get_object_or_404(Address, pk=pk)
        
    message = ''
    if request.method == 'POST':
        form = AddressForm(request.POST,request.FILES,instance=instance)
        
        if form.is_valid():
            
            #update product
            data = form.save(commit=False)
            data.date_updated = datetime.datetime.today()
            data.updater = request.user
            data.save()
                    
            response_data = {
                "status": "true",
                "title": "Successfully Updated",
                "message": "Address Update successfully.",
                'redirect': 'true',
                "redirect_url": reverse('web:address')
            }
    
        else:
            message = generate_form_errors(form ,formset=False)
            
            
            response_data = {
                "status": "false",
                "title": "Failed",
                "message": message
            }

        return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    
    else:
        
        form = AddressForm(instance=instance)

        context = {
            'form': form,
            'page_name' : 'Update Address',
            'page_title' : 'Update Address',
            'is_need_select2' : True,
            'url' : reverse('web:address'),
        }

        return render(request, 'admin_panel/create/create.html',context)


@login_required
@role_required(['superadmin'])
def delete_address_view(request, pk):
    """
    Address deletion, it only mark as is deleted field to true
    :param request:
    :param pk:
    :return:
    """
    Address.objects.filter(pk=pk).update(is_deleted=True)

    response_data = {
        "status": "true",
        "title": "Successfully Deleted",
        "message": "Address Successfully Deleted.",
        "redirect": "true",
        "redirect_url": reverse('web:address')
    }

    return HttpResponse(json.dumps(response_data), content_type='application/javascript')




@login_required
@role_required(['superadmin'])
def connect_view(request):
    """
    Connect listings
    :param request:
    :return: Connect list view
    """
    instances = Connect.objects.filter(is_deleted=False).order_by("-id")
    
    filter_data = {}
    query = request.GET.get("q")
    
    if query:

        instances = instances.filter(
            Q(auto_id__icontains=query) |
            Q(name__icontains=query) 
        )
        title = "Connect - %s" % query
        filter_data['q'] = query
    

    context = {
        'instances': instances,
        'page_name' : 'Connect',
        'page_title' : 'Connect',
        'filter_data' :filter_data,
    }

    return render(request, 'admin_panel/product/connect_list.html', context)


@login_required
@role_required(['superadmin'])
def create_connect_view(request):
    """
    create operation of Connect
    :param request:
    :param pk:
    :return:
    """
    if request.method == 'POST':
        # if instance go to edit
        form = ConnectForm(request.POST,request.FILES,request.FILES)
            
        if form.is_valid():
            data = form.save(commit=False)
            data.auto_id = get_auto_id(Connect)
            data.creator = request.user
            data.date_updated = datetime.datetime.today()
            data.updater = request.user
            data.save()

            response_data = {
                "status": "true",
                "title": "Successfully Created",
                "message": "Connect created successfully.",
                'redirect': 'true',
                "redirect_url": reverse('web:connect')
            }
    
        else:
            message =generate_form_errors(form , formset=False)
            response_data = {
                "status": "false",
                "title": "Failed",
                "message": message,
            }

        return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    
    else:
        
        form = ConnectForm()

        context = {
            'form': form,
            'page_name' : 'Create Connect',
            'page_title' : 'Create Connect',
            'url' : reverse('web:create_connect'),
        }

        return render(request, 'admin_panel/create/create.html',context)

    
@login_required
@role_required(['superadmin'])
def edit_connect_view(request,pk):
    """
    edit operation of Connect
    :param request:
    :param pk:
    :return:
    """
    instance = get_object_or_404(Connect, pk=pk)
        
    message = ''
    if request.method == 'POST':
        form = ConnectForm(request.POST,request.FILES,instance=instance)
        
        if form.is_valid():
            
            #update product
            data = form.save(commit=False)
            data.date_updated = datetime.datetime.today()
            data.updater = request.user
            data.save()
                    
            response_data = {
                "status": "true",
                "title": "Successfully Updated",
                "message": "Connect Update successfully.",
                'redirect': 'true',
                "redirect_url": reverse('web:connect')
            }
    
        else:
            message = generate_form_errors(form ,formset=False)
            
            
            response_data = {
                "status": "false",
                "title": "Failed",
                "message": message
            }

        return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    
    else:
        
        form = ConnectForm(instance=instance)

        context = {
            'form': form,
            'page_name' : 'Update Connect',
            'page_title' : 'Update Connect',
            'is_need_select2' : True,
            'url' : reverse('web:connect'),
        }

        return render(request, 'admin_panel/create/create.html',context)


@login_required
@role_required(['superadmin'])
def delete_connect_view(request, pk):
    """
    Connect deletion, it only mark as is deleted field to true
    :param request:
    :param pk:
    :return:
    """
    Connect.objects.filter(pk=pk).update(is_deleted=True)

    response_data = {
        "status": "true",
        "title": "Successfully Deleted",
        "message": "Connect Successfully Deleted.",
        "redirect": "true",
        "redirect_url": reverse('web:connect')
    }

    return HttpResponse(json.dumps(response_data), content_type='application/javascript')



@login_required
@role_required(['superadmin'])
def description_view(request):
    """
    Description listings
    :param request:
    :return: Description list view
    """
    instance = Description.objects.filter(is_deleted=False).order_by("-id").first()
    
    

    context = {
        'instance': instance,
        'page_name' : 'Description',
        'page_title' : 'Description',
    }

    return render(request, 'admin_panel/product/description.html', context)


@login_required
@role_required(['superadmin'])
def create_description_view(request):
    """
    create operation of Description
    :param request:
    :param pk:
    :return:
    """
    if request.method == 'POST':
        # if instance go to edit
        form = DescriptionForm(request.POST,request.FILES,request.FILES)
            
        if form.is_valid():
            data = form.save(commit=False)
            data.auto_id = get_auto_id(Description)
            data.creator = request.user
            data.date_updated = datetime.datetime.today()
            data.updater = request.user
            data.save()

            response_data = {
                "status": "true",
                "title": "Successfully Created",
                "message": "Description created successfully.",
                'redirect': 'true',
                "redirect_url": reverse('web:description')
            }
    
        else:
            message =generate_form_errors(form , formset=False)
            response_data = {
                "status": "false",
                "title": "Failed",
                "message": message,
            }

        return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    
    else:
        
        form = DescriptionForm()

        context = {
            'form': form,
            'page_name' : 'Create Description',
            'page_title' : 'Create Description',
            'url' : reverse('web:create_description'),
        }

        return render(request, 'admin_panel/create/create.html',context)

    
@login_required
@role_required(['superadmin'])
def edit_description_view(request,pk):
    """
    edit operation of Description
    :param request:
    :param pk:
    :return:
    """
    instance = get_object_or_404(Description, pk=pk)
        
    message = ''
    if request.method == 'POST':
        form = DescriptionForm(request.POST,request.FILES,instance=instance)
        
        if form.is_valid():
            
            #update product
            data = form.save(commit=False)
            data.date_updated = datetime.datetime.today()
            data.updater = request.user
            data.save()
                    
            response_data = {
                "status": "true",
                "title": "Successfully Updated",
                "message": "Description Update successfully.",
                'redirect': 'true',
                "redirect_url": reverse('web:description')
            }
    
        else:
            message = generate_form_errors(form ,formset=False)
            
            
            response_data = {
                "status": "false",
                "title": "Failed",
                "message": message
            }

        return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    
    else:
        
        form = DescriptionForm(instance=instance)

        context = {
            'form': form,
            'page_name' : 'Update Description',
            'page_title' : 'Update Description',
            'is_need_select2' : True,
            'url' : reverse('web:description'),
        }

        return render(request, 'admin_panel/create/create.html',context)

#************************************************************************************************************
#**********************************web views start***********************************************************



def index(request):
    categories = Category.objects.filter(is_deleted=False).order_by("-id")
    instances = Service.objects.filter(is_deleted=False).order_by("-id")
    careers = Career.objects.filter(is_deleted=False).order_by("date_added")
    teams = TeamMember.objects.filter(is_deleted=False).order_by("date_added")
    about_us = AboutUs.objects.filter(is_deleted=False).order_by("date_added")
    testimonial = Testimonial.objects.filter(is_deleted=False).order_by("date_added")
    main_address = Address.objects.filter(office_type="main_office",is_deleted=False).order_by("date_added").first()
    sub_address = Address.objects.filter(office_type="sub_office",is_deleted=False).order_by("date_added").first()
    connect = Connect.objects.filter(is_deleted=False).order_by("date_added").first()
    descriptions = Description.objects.filter(is_deleted=False).order_by("date_added").first()
    
    

    context = {
        'categories': categories, # instance for categories
        'instances': instances, # instance for services
        'careers': careers, # instance for careers
        'teams': teams, # instance for teams
        'about_us': about_us, # instance for about us
        'testimonial': testimonial, # instance for testimonial
        'main_address': main_address, # instance for main_address
        'sub_address': sub_address, # instance for sub_address
        'connect': connect, # instance for connect
        'descriptions': descriptions, # instance for descriptions
    }

    return render(request, 'web/index.html',context)


def product_category_view(request):
    response_data = {}
    category = request.GET.get("category")
    print(category)
    category_instance = Category.objects.get(pk=category)
    if Product.objects.filter(category__pk=category,is_deleted=False).exists():
        data = []
        product_instances = Product.objects.filter(category__pk=category,is_deleted=False)
        for product in product_instances:
            data.append({
                'name': product.name,
                'color': product.color,
                'image': product.image.url,
            })
        response_data = {
            "status": "6000",
            "product_instances": data,
            'c_desctription_title': category_instance.description_title,
            'c_desctription_description': category_instance.description,
        }
        
    else:
        message = "no products in this category"
        print(message)
        
        response_data = {
            "status": "6001",
            "message" : message,
        }

    return HttpResponse(json.dumps(response_data), content_type='application/javascript')