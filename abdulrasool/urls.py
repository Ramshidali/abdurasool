from django.contrib import admin
from django.views.static import serve
from django.urls import include, path, re_path
from abdulrasool import settings
from main import views as general_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/accounts/', include('registration.backends.default.urls')),
    path('super-admin/',include(('main.urls'),namespace='main')),
    path('super-admin/',general_views.app,name='app'),
    
    # admin panel
    path('super-admin/product/',include(('product.urls'),namespace='product')),
    path('super-admin/web/',include(('web.urls'),namespace='web')),
    
    # web
    path('', include('web.urls', namespace="web")),    
    
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT})
]
