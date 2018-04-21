from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .api_view import HumanList, HumanDetail


app_name = 'api'
urlpatterns = [
    path('', HumanList.as_view(), name='human_list'),
    path('<int:pk>', HumanDetail.as_view(), name='human_detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)
