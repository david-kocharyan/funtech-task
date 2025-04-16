from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include, re_path
from django.views.generic import RedirectView
from django.contrib import admin
from django.contrib.staticfiles.storage import staticfiles_storage

from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from apps.core.settings import BothHttpAndHttpsSchemaGenerator

urlpatterns = [
    # Admin
    path('', RedirectView.as_view(url='/admin')),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('favicon.ico'))),
    path('admin/', admin.site.urls),

    # User
    path('v1/users/', include('apps.users.urls', namespace='users')),
]

if settings.ENVIRONMENT == "development":
    schema_view = get_schema_view(
        openapi.Info(
            title="Funtech test task API",
            default_version='v1',
        ),
        public=True,
        generator_class=BothHttpAndHttpsSchemaGenerator,
        permission_classes=[permissions.AllowAny],
    )
    urlpatterns += [
        re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
        re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
