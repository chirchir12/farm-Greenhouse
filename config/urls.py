from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', include('pages.urls')),
    path('', include('products.urls')),
    path('news/', include('news.urls')),
     path('careers/', include('careers.urls')),
     path('projects/', include('projects.urls')),
    path('products/search', include('search.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    # path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
]



if settings.DEBUG:
    urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
