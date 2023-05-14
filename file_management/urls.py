from django.urls import path
from .views import ContentCreateView, ContentDownloadView, ContentListAPIView, ContentDetailView

urlpatterns = [
    path('upload/', ContentCreateView.as_view(), name='file_upload'),
    path('download/<int:content_id>/', ContentDownloadView.as_view(), name='file_download'),
    path('list/<int:module_id>/', ContentListAPIView.as_view(), name='file_list'),
    path('content/<int:pk>/', ContentDetailView.as_view(), name='content_detail'),
]