# Create your views here.
from rest_framework import viewsets
from rest_framework_gis.filters import DistanceToPointFilter, InBBoxFilter
from rest_framework.pagination import PageNumberPagination

from .serializers import ShelterSerializer
from .models import Shelter

from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import traceback
import json
from django.core.serializers import serialize

from django.shortcuts import render
from django.http import HttpResponse

class MyPagination(PageNumberPagination):
    page_size_query_param = 'page_size'

class ShelterViewSet(viewsets.ModelViewSet):
    queryset = Shelter.objects.all()
    serializer_class = ShelterSerializer
    pagination_class = MyPagination
    filter_backends = (DistanceToPointFilter,)
    distance_filter_field = 'geom'
    distance_filter_convert_meters = True

class ProgressShelter(APIView):
    def get(self, request, *args, **keywords):
        try:
            queryset = Shelter.objects.raw('select s.id, replace(s.name, \'　\', \' \') as name, floor(COALESCE(p.finish_rate,0) * 100) as finish_rate, floor(COALESCE(p.waiting_rate, 0)*100) as waiting_rate, floor(COALESCE(p.working_rate,0)*100) as working_rate, s.geom  from shelter as s left join progress as p on (s.id = p.shelter_id)')
            encjson = serialize('geojson', queryset, srid=4326, geometry_field='geom', fields=('name', 'finish_rate', 'waiting_rate', 'working_rate',) )
            result   = json.loads(encjson)
            response = Response(result, status=status.HTTP_200_OK)
        except Exception as e:
            traceback.print_exc()
            response = Response({}, status=status.HTTP_404_NOT_FOUND)
        except:
            response = Response({}, status=status.HTTP_404_NOT_FOUND)
        return response



class GeojsonSQLAPIView(APIView):
    def get(self, request, *args, **keywords):
        try:
            encjson  = serialize('geojson', Shelter.objects.all(), srid=4326, geometry_field='geom', fields=('name','description',) )
            result   = json.loads(encjson)
            response = Response(result, status=status.HTTP_200_OK)
        except Exception as e:
            traceback.print_exc()
            response = Response({}, status=status.HTTP_404_NOT_FOUND)
        except:
            response = Response({}, status=status.HTTP_404_NOT_FOUND)
        return response

class GeojsonAPIView(APIView):
    def get(self, request, *args, **keywords):
        try:
            encjson  = serialize('geojson', Shelter.objects.all(), srid=4326, geometry_field='geom', fields=('name','description',) )
            result   = json.loads(encjson)
            response = Response(result, status=status.HTTP_200_OK)
        except Exception as e:
            traceback.print_exc()
            response = Response({}, status=status.HTTP_404_NOT_FOUND)
        except:
            response = Response({}, status=status.HTTP_404_NOT_FOUND)
        return response

def index(request):
    contexts = {}
    return render(request,'shelter/index.html',contexts)

def hq(request):
    contexts = {}
    return render(request, 'shelter/hq.html', contexts)

def req(request):
    contexts = {}
    return render(request, 'shelter/req.html', contexts)

def shelter_list(request):
    return HttpResponse('list')

def shelter_edit(request):
    return HttpResponse('edit')

def shelter_delete(request):
    return HttpResponse('delete')
