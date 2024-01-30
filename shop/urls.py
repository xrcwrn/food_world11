from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views
from django.conf import settings


urlpatterns = [
path('',views.getItems),
path('items/',views.getItems),
path('post/',views.postItem),
path('item/<int:id>', views.getItem),
path('update/<int:id>',views.update),
path('delete/<int:id>',views.delete),

#jwt authentication
 path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
 path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
