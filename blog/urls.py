#from django.urls import include,URLPattern
from django.urls import include, path
from django.urls import re_path
from django.urls import re_path as url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.HomePageView.as_view(), name='HomePageView'),

    
    #url(r'^', include('blog.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

