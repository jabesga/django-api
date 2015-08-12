from django.conf.urls import patterns, include, url
from django.contrib import admin
#from rest_framework import routers
#from quickstart import views


#router = routers.DefaultRouter()
#router.register(r'users', views.UserViewSet)
#router.register(r'groups', views.GroupViewSet)

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^api/v1/', include('api.urls')),
                       #url(r'^router/', include(router.urls)),
                       #url(r'^quickstart/', include('quickstart.urls')),
                       #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
                       )
