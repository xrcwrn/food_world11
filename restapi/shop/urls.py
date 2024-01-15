from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
path('',views.getItems),
path('items/',views.getItems),
path('post/',views.postItem),
path('item/<int:id>', views.getItem),
path('update/<int:id>',views.update),
path('delete/<int:id>',views.delete),

 #Authentication
    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
