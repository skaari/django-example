from django.urls import path
# from django.conf.urls import url
from template_app import views

#TEmplate tagging
app_name="template_app"
urlpatterns=[
    path('relative/',views.relative, name='relative'),
    path('other/',views.other,name='other')
]
