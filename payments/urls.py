from django.urls import path
from .views import my_copun, start_trans, add_copun

urlpatterns = [
    path('my_copun/<str:email>/', my_copun, name='my_copun'),
    path('start_trans/<str:dargah>/<int:fac_id>/', start_trans, name='start_trans'),
    path('add_copun/<int:transID>/<str:email>/<str:code>/', add_copun, name='add_copun'),
]