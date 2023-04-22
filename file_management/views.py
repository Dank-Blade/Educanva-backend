from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
# from rest_framework.permissions import isAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import File
from .serializers import FileSerializer
from django.http import HttpResponse, Http404
from django.conf import settings
from django.views import View
import os

class FileUploadView(APIView):
    # permission_classes = (isAuthenticated)
    
    
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FileDownloadView(View):
    # permission_classes = (isAuthenticated)
    def get(self, request, file_name):
        file_path = os.path.join(settings.MEDIA_ROOT, file_name)
        if os.path.exists(file_path):
            with open(file_path, 'rb') as fh:
                response = HttpResponse(fh.read(), content_type="application/octet-stream")
                response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
                return response
        raise Http404