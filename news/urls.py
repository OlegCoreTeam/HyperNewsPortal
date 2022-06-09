from django.urls import path, re_path
from news.views import MainPageView, NewsPageView, PostView, PostCreateView


urlpatterns = [
    path('', MainPageView.as_view()),
    path('news/', NewsPageView.as_view(), name='news'),
    re_path("news/(?P<link>[^/]*\\d)/?", PostView.as_view()),
    path("news/create/", PostCreateView.as_view(), name='post_create')
]
