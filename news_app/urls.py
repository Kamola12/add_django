
from .views import HomePageView, news_list,news_detail,UzbekistanPage,SportPage
from django.urls import path,include

urlpatterns=[
    path('',HomePageView,name="homepage"),
    path('news/',news_list,name="news_all"),
    path("news/<int:id>/",news_detail,name='news_detail_page'),
    path('uzbekistan/',UzbekistanPage,name="uzbekistan"),
    path('sport/',SportPage,name="sport")

]