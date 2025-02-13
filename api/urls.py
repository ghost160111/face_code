from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from example import views
from django.conf.urls.i18n import i18n_patterns
from example.views import index

# handler404 = views.PageNotFound
# handler403 = views.ForbiddenPage

urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('api/', include('example.urls')),
]

urlpatterns += i18n_patterns(
    # Add your i18n patterns here
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
