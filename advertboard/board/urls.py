from django.urls import path
from .views import AdsList, AdsDetail, AdsCreate, AdsDelete, AdsUpdate, RespDelete, MailingCreate, save_comment

urlpatterns = [
    path('', AdsList.as_view(), name='board'),
    path('<int:pk>', AdsDetail.as_view(), name='adsdetail'),
    path('adscreate/', AdsCreate.as_view(), name='adscreate'),
    path('<int:pk>/adsdelete/', AdsDelete.as_view(), name='adsdelete'),
    path('<int:pk>/adsupdate/', AdsUpdate.as_view(), name='adsupdate'),
    path('<int:pk>/respdelete/', RespDelete.as_view(), name='respdelete'),
    path('savecomment/', save_comment, name='savecomment'),
    path('mailing/', MailingCreate.as_view(), name='mailing'),
]
