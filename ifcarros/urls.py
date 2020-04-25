from django.urls import path
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.views import get_swagger_view
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer
# from django.conf.urls.i18n import i18n_patterns

# schema_view = get_schema_view(title='MINHA API')
schema_view = get_swagger_view(title='IF Carros')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('api.urls')),
    url(r'^conta/', include('django.contrib.auth.urls')),
    url(r'^swagger', schema_view),
    url(r'^web/', include('web.urls')),
]

# urlpatterns += ([
#     path("", include('base.urls'))
# ]) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)