import datetime
import json
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.urls import reverse

from main.decorators import role_required
from main.functions import generate_form_errors, get_auto_id, paginate
from product.forms import CategoryForm, ProductForm
from product.models import Category, Product

# Create your views here.

@login_required
@role_required(['superadmin'])
def category_single_view(request,pk):
    """
    category sigle view
    :param request:
    :return: category list view
    """
    instance = Category.objects.get(pk=pk,is_deleted=False)

    context = {
        'instance': instance,
        'page_name' : 'Category',
        'page_title' : 'Category',
        'active_page_name' : 'Category single view',
    }

    return render(request, 'admin_panel/product/single_view.html', context)


@login_required
@role_required(['superadmin'])
def category_view(request):
    """
    category listings
    :param request:
    :return: category list view
    """
    instances = Category.objects.filter(is_deleted=False).order_by("-id")
    
    filter_data = {}
    query = request.GET.get("q")
    
    if query:

        instances = instances.filter(
            Q(auto_id__icontains=query) |
            Q(name__icontains=query) 
        )
        title = "Category - %s" % query
        filter_data['q'] = query
    

    context = {
        'instances': instances,
        'page_name' : 'Category',
        'page_title' : 'Category',
        'filter_data' :filter_data,
    }

    return render(request, 'admin_panel/product/category.html', context)


@login_required
@role_required(['superadmin'])
def create_category_view(request):
    """
    create operation of category
    :param request:
    :param pk:
    :return:
    """
    if request.method == 'POST':
        # if instance go to edit
        form = CategoryForm(request.POST,request.FILES)
            
        if form.is_valid():
            data = form.save(commit=False)
            data.auto_id = get_auto_id(Category)
            data.creator = request.user
            data.date_updated = datetime.datetime.today()
            data.updater = request.user
            data.save()

            response_data = {
                "status": "true",
                "title": "Successfully Created",
                "message": "Category created successfully.",
                'redirect': 'true',
                "redirect_url": reverse('product:category')
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
        
        form = CategoryForm()

        context = {
            'form': form,
            'page_name' : 'Create Category',
            'page_title' : 'Create Category',
            'url' : reverse('product:create_category'),
        }

        return render(request, 'admin_panel/create/create.html',context)

    
@login_required
@role_required(['superadmin'])
def edit_category_view(request,pk):
    """
    edit operation of category
    :param request:
    :param pk:
    :return:
    """
    instance = get_object_or_404(Category, pk=pk)
        
    message = ''
    if request.method == 'POST':
        form = CategoryForm(request.POST,request.FILES,instance=instance)
        
        if form.is_valid():
            
            #update meta keyword
            data = form.save(commit=False)
            data.date_updated = datetime.datetime.today()
            data.updater = request.user
            data.save()
                    
            response_data = {
                "status": "true",
                "title": "Successfully Created",
                "message": "Category Update successfully.",
                'redirect': 'true',
                "redirect_url": reverse('product:category')
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
        
        form = CategoryForm(instance=instance)

        context = {
            'form': form,
            'page_name' : 'Update Category',
            'page_title' : 'Update Category',
            'is_need_select2' : True,
            'url' : reverse('product:category'),
        }

        return render(request, 'admin_panel/create/create.html',context)


@login_required
@role_required(['superadmin'])
def delete_category_view(request, pk):
    """
    category deletion, it only mark as is deleted field to true
    :param request:
    :param pk:
    :return:
    """
    Category.objects.filter(pk=pk).update(is_deleted=True)

    response_data = {
        "status": "true",
        "title": "Successfully Deleted",
        "message": "Category Successfully Deleted.",
        "redirect": "true",
        "redirect_url": reverse('product:category')
    }

    return HttpResponse(json.dumps(response_data), content_type='application/javascript')


@login_required
@role_required(['superadmin'])
def product_single_view(request,pk):
    """
    product sigle view
    :param request:
    :return: category list view
    """
    instance = Product.objects.get(pk=pk,is_deleted=False)

    context = {
        'instance': instance,
        'page_name' : 'Product',
        'page_title' : 'Product',
        'active_page_name' : 'Product single view',
    }

    return render(request, 'admin_panel/product/single_view.html', context)


@login_required
@role_required(['superadmin'])
def product_view(request):
    """
    product listings
    :param request:
    :return: product list view
    """
    instances = Product.objects.filter(is_deleted=False).order_by("-id")
    
    filter_data = {}
    query = request.GET.get("q")
    
    if query:

        instances = instances.filter(
            Q(auto_id__icontains=query) |
            Q(name__icontains=query) 
        )
        title = "Category - %s" % query
        filter_data['q'] = query
    

    context = {
        'instances': instances,
        'page_name' : 'Products',
        'page_title' : 'Products',
        'filter_data' :filter_data,
    }

    return render(request, 'admin_panel/product/product_list.html', context)


@login_required
@role_required(['superadmin'])
def create_product_view(request):
    """
    create operation of product
    :param request:
    :param pk:
    :return:
    """
    if request.method == 'POST':
        # if instance go to edit
        form = ProductForm(request.POST,request.FILES)
            
        if form.is_valid():
            data = form.save(commit=False)
            data.auto_id = get_auto_id(Product)
            data.creator = request.user
            data.date_updated = datetime.datetime.today()
            data.updater = request.user
            data.save()

            response_data = {
                "status": "true",
                "title": "Successfully Created",
                "message": "Product created successfully.",
                'redirect': 'true',
                "redirect_url": reverse('product:product')
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
        
        form = ProductForm()

        context = {
            'form': form,
            'page_name' : 'Create Product',
            'page_title' : 'Create Product',
            'url' : reverse('product:create_product'),
        }

        return render(request, 'admin_panel/create/create.html',context)

    
@login_required
@role_required(['superadmin'])
def edit_product_view(request,pk):
    """
    edit operation of product
    :param request:
    :param pk:
    :return:
    """
    instance = get_object_or_404(Product, pk=pk)
        
    message = ''
    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES,instance=instance)
        
        if form.is_valid():
            
            #update product
            data = form.save(commit=False)
            data.date_updated = datetime.datetime.today()
            data.updater = request.user
            data.save()
                    
            response_data = {
                "status": "true",
                "title": "Successfully Created",
                "message": "Product Update successfully.",
                'redirect': 'true',
                "redirect_url": reverse('product:product')
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
        
        form = ProductForm(instance=instance)

        context = {
            'form': form,
            'page_name' : 'Update Product',
            'page_title' : 'Update Product',
            'is_need_select2' : True,
            'url' : reverse('product:product'),
        }

        return render(request, 'admin_panel/create/create.html',context)


@login_required
@role_required(['superadmin'])
def delete_product_view(request, pk):
    """
    product deletion, it only mark as is deleted field to true
    :param request:
    :param pk:
    :return:
    """
    Product.objects.filter(pk=pk).update(is_deleted=True)

    response_data = {
        "status": "true",
        "title": "Successfully Deleted",
        "message": "Product Successfully Deleted.",
        "redirect": "true",
        "redirect_url": reverse('product:product')
    }

    return HttpResponse(json.dumps(response_data), content_type='application/javascript')
