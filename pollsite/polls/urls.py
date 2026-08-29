from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path("<int:pk>/delete", views.delete_question, name="delete"),
    path("search/", views.SearchView.as_view(), name="search"),
    path("login/", views.login_view, name="login")
]
