from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import *
...

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [

 path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   path('s/',TashxisStats.as_view()),
   path('a',Statistikaa.as_view()),
   path('w/',statistika),
   path('q/',St.as_view()),
   # path('bemor/create/', BemorCreateAPIView.as_view(), name='bemor-create'),
   #  path('tashxis/create/', TashxisCreateAPIView.as_view(), name='tashxis-create'),
   #  path('bemor/detail/<int:pk>/', BemorDetailAPIView.as_view(), name='bemor-detail'),
   #  path('tashxis/detail/<int:pk>/', TashxisDetailAPIView.as_view(), name='tashxis-detail'),
   #  path('statistika/',TashxisStatisticsAPIView.as_view()),
    path('q/<int:pk>/',TashxisDetail.as_view()),
   #  path('ta/<int:bemor_id>/',TashxisSoniView.as_view())



]
