from django.contrib import admin
from IT_company import views as it_company_views
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'it_company', it_company_views.ITCompanyViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('admin/', admin.site.urls),
]