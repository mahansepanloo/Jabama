from django.urls import path
from .views import ListJa, Rateing, InfoJa, ManageJa

urlpatterns = [
    path('ja', ListJa.as_view(), name='list-create-ja'),
    path('rate', Rateing.as_view(), name='list-create-rate'),
    path('ja/<int:pk>', InfoJa.as_view(), name='retrieve-ja'),
    path('ja/manage/<int:pk>', ManageJa.as_view(), name='manage-ja'),
]