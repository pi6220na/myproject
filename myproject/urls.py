from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.contrib import admin
from myapp import views
# admin.autodiscover()
app_name = 'myapp'
# namespace='myapp'
urlpatterns = [
    url(r'^', include('myapp.urls',namespace="myapp") ),
    url(r'^admin/', admin.site.urls),    #Admin site
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



