from django.urls import path

from .views import ContributorList, ContributorDetail

urlpatterns = [
    path('<int:pk>/', ContributorDetail.as_view()),
    path('', ContributorList.as_view()),
]