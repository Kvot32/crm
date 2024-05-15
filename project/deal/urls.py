from django.urls import path
from .views import deal_list, created_deal

app_name = 'deal'

urlpatterns = [
    path('', deal_list, name = 'deals'),
    path('created_deal/', created_deal, name = 'created_deal'),
]