from django.urls import path

from .views import RewardList, RewardDetail

urlpatterns = [
    path('<int:pk>/', RewardDetail.as_view()),
    path('', RewardList.as_view()),
]