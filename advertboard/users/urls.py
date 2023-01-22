from django.urls import path
from .views import ProfileView, AdsView, RespView, accept_response

urlpatterns = [
    path('', ProfileView.as_view(), name='userprofile'),
    path('ads/',AdsView.as_view(), name='userads'),
    path('resp/',RespView.as_view(), name='userresp'),
    path('acceptresponse/', accept_response, name='acceptresponse'),
]
