from django.urls import path
from .views import RegisterView, MyTokenObtainPairView, UserView, UserDetailView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('api/login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', RegisterView.as_view(), name="sign_up"),
    path('api/users/', UserView.as_view(), name="users"),
    path('api/users/<int:pk>/', UserDetailView.as_view(), name="user_detail"),
    # path('api/users/delete/<int:pk>/', UserDelete.as_view(), name='delete_user'),
]
