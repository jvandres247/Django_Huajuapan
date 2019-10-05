from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin


from django.views.generic import TemplateView

urlpatterns = [
    # Django administration site
    path('admin/', admin.site.urls),
    # Index template
    path('', TemplateView.as_view(template_name='pages/landing.html'), name='index'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)