from django.urls import path

from . import views

app_name = 'audiobooks'

urlpatterns = [
    # path("", views.index, name = 'index'),
    path("", views.IndexView.as_view(), name = 'index'),

    # path('<int:audiobook_id>/', views.details, name = 'details'),
    path('<int:pk>/', views.DetailsView.as_view(), name = 'details'),

    path("<int:audiobook_id>/review/", views.review, name = 'review'),

    # path("<int:audiobook_id>/results/", views.results, name = 'results'),
    path("<int:pk>/results", views.ResultsView.as_view(), name = 'results'),
]