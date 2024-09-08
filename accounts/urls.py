from django.urls import path
from .views import ShowListUser, ShowInfoUser, CreateUser, Edit, Login, DeletUser

urlpatterns = [
    path('users', ShowListUser.as_view(), name='user-list'),
    path('users/me', ShowInfoUser.as_view(), name='user-info'),
    path('users/create', CreateUser.as_view(), name='user-create'),
    path('users/<int:pk>', Edit.as_view(), name='user-edit'),
    path('users/delete/<int:pk>', DeletUser.as_view(), name='user-delete'),
    path('log', Login.as_view(), name='login'),

]