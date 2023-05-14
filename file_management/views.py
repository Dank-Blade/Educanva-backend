from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
# from rest_framework.permissions import isAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import File
from module.models import Module
from .serializers import FileSerializer
from django.http import HttpResponse, Http404, FileResponse
from django.conf import settings
from django.views import View
from rest_framework import permissions
from rest_framework import generics

import os

class ContentCreateView(generics.CreateAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    # def perform_create(self, serializer):
    #     module_id = self.kwargs.get('module_id')
    #     module = Module.objects.get(id=module_id)
    #     serializer.save(module=module, uploaded_by=self.request.user)
    
    def post(self, request, *args, **kwargs):
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class ContentListAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FileSerializer

    def get_queryset(self):
        module_id = self.kwargs['module_id']
        return File.objects.filter(module_id=module_id)

class ContentDownloadView(generics.RetrieveAPIView):
    # queryset = File.objects.all()
    # serializer_class = FileSerializer
    # permission_classes = [permissions.IsAuthenticated]

    # def get(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     module = instance.module
    #     user = request.user
    #     if user not in module.users.all():
    #         return Response({'detail': 'You are not enrolled in this module.'}, status=status.HTTP_403_FORBIDDEN)
    #     file_path = instance.file.path
    #     response = FileResponse(open(file_path, 'rb'), content_type='application/octet-stream')
    #     response['Content-Disposition'] = 'attachment; filename="%s"' % instance.file.name
    #     return response
    
    # def get(self, request, file_name):
    #     file_path = os.path.join(settings.MEDIA_ROOT, file_name)
    #     if os.path.exists(file_path):
    #         with open(file_path, 'rb') as fh:
    #             response = HttpResponse(fh.read(), content_type="application/octet-stream")
    #             response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
    #             return response
    #     raise Http404
    
    # def get(self, request, content_id):
    #     try:
    #         content_file = File.objects.get(id=content_id)
    #     except File.DoesNotExist:
    #         raise Http404

    #     file_path = content_file.file.path
    #     if os.path.exists(file_path):
    #         with open(file_path, 'rb') as fh:
    #             response = HttpResponse(fh.read(), content_type='application/pdf')
    #             response['Content-Disposition'] = f'attachment; filename={content_file.name}'
    #             return response
    #     raise Http404
    
    def get(self, request, pk):
        try:
            file_object = File.objects.get(pk=pk)
        except File.DoesNotExist:
            raise Http404

        file_path = file_object.file.path
        if os.path.exists(file_path):
            with open(file_path, 'rb') as fh:
                file_content = fh.read()
        else:
            raise Http404

        serializer = FileSerializer(file_object)
        response_data = serializer.data
        response_data['file'] = file_content
        response = Response(response_data)

        response['Content-Disposition'] = f'attachment; filename={file_object.name}'
        return response
    
class ContentDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            return File.objects.get(pk=pk)
        except File.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        content = self.get_object(pk)
        file_path = content.file.path
        response = FileResponse(open(file_path, 'rb'))
        response['content_type'] = 'application/pdf'
        response['Content-Disposition'] = f'attachment; filename="{content.file.name}"'
        return response

    def delete(self, request, pk, format=None):
        content = self.get_object(pk)
        content.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)