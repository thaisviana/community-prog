from django.conf.urls import url
from django.contrib import admin
from community import views as views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='home'),
    url(r'^categories/', views.categories, name='categories'),
    url(r'^contents/id/(\d+)', views.contents, name='contents'),
    url(r'^content/video/(\d+)', views.video_content, name='video_content'),
    url(r'^content/pdf/(\d+)', views.pdf_content, name='pdf_content'),
    url(r'^events/', views.events, name='events'),
    url(r'^projects/', views.projects, name='projects')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)