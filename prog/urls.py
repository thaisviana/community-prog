from django.conf.urls import url
from django.contrib import admin
from community import views as views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='home')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)