from django.contrib.gis import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from shelter.views import ShelterViewSet, index, hq, req, GeojsonAPIView, ProgressShelter
from django.views.generic.base import RedirectView

from shelter import views

from websocket import urls as websocket_urls

router = DefaultRouter()
router.register('shelter', ShelterViewSet)

urlpatterns = [
    path('request/', include(('request.urls','request'), namespace='request')),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', index, name='shelter_index'),
    path('socket/', include(websocket_urls)),
    path('hq', hq, name='shelter_hq'),
    path('req', req ,name='shelter_req'),

    path('shelter/geojson/', GeojsonAPIView.as_view(), name='geojson_view'),
    path('shelter/progress/', ProgressShelter.as_view(), name='progress_view'),

    path('shelter/', views.shelter_list, name='shelter_list'),
    path('shelter/add', views.shelter_edit, name='shelter_add'),
    path('shelter/edit/<int:id>', views.shelter_edit, name='shelter_edit'),
    path('shelter/delete/<int:id>', views.shelter_delete, name='shelter_delete'),

]
