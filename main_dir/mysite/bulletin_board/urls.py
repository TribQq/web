from django.urls import path
from .views import *


urlpatterns = [
    path('note', NoteView.as_view(), name='Note'),

    path('', index1, name='top10'),
    path('<str:page>/', other_page, name='other'),
    path('accounts/login/', BBLoginView.as_view(), name='login'),
    path('accounts/logout/', BBLogoutView.as_view(), name='logout'),
    path('accounts/profile/change/', ChangeUserInfoView.as_view(), name='change_profile'),
    path('accounts/profile/', profile, name='profile'),



]