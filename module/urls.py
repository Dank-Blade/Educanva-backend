from django.urls import path
from .views import CreateModule, ModuleView, ModuleDetailView

urlpatterns = [
    path('api/create/', CreateModule.as_view(), name='create_module'),
    path('api/module/', ModuleView.as_view(), name='module_list'),
    path('api/module/<int:pk>/', ModuleDetailView.as_view(), name='module_detail'),
]
