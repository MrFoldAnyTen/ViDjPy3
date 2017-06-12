from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^hey/', views.index, name='index'),
#    url(r'^webapp/', include('webapp.urls')),
]
