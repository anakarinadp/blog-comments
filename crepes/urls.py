from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('blog/', include('blog.urls')), # url(r'^blog/', include('blog.urls')),
	path('admin/', admin.site.urls, name='admin'), # url(r'^admin/', include(admin.site.urls)),
]