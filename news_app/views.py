from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.shortcuts import render,get_object_or_404
from .models import News, Category
# Create your views here.

def news_list(request):
    news_list = News.objects.filter(status=News.Status.Published)

    context = {'news_list' : news_list}
    return render(request, "news/news_list.html", context=context)


def news_detail(request,id):
    news=get_object_or_404(News,id=id,status=News.Status.Published)
    context={'news':news}
    return render(request,'news/news_detail.html',context=context)

def HomePageView(request):
    categories=Category.objects.all()
    news_list=News.published.all().order_by('-publish_time')[:3]
    local_1 = News.published.all().filter(category__name='Uzbekistan').order_by("-publish_time")[1]
    local_2 = News.published.all().filter(category__name='Uzbekistan').order_by("-publish_time")[2]
    local_3 = News.published.all().filter(category__name='Uzbekistan').order_by("-publish_time")[3]
    local_4 = News.published.all().filter(category__name='Uzbekistan').order_by("-publish_time")[4]
    local_5 = News.published.all().filter(category__name='Uzbekistan').order_by("-publish_time")[5]
    sport_1 = News.published.all().filter(category__name='sport').order_by("-publish_time")[1]
    sport_2 = News.published.all().filter(category__name='sport').order_by("-publish_time")[2]
    sport_3 = News.published.all().filter(category__name='sport').order_by("-publish_time")[3]
    sport_4 = News.published.all().filter(category__name='sport').order_by("-publish_time")[4]
    jahon_one = News.published.all().filter(category__name='jahon').order_by("-publish_time")
    fan_texnika1 = News.published.all().filter(category__name='fan-texnika').order_by("-publish_time")[1]
    fan_texnika2 = News.published.all().filter(category__name='fan-texnika').order_by("-publish_time")[2]
    fan_texnika3 = News.published.all().filter(category__name='fan-texnika').order_by("-publish_time")[3]
    fan_texnika4 = News.published.all().filter(category__name='fan-texnika').order_by("-publish_time")[4]
    jahon1 = News.published.all().filter(category__name='jahon').order_by("-publish_time")[0]
    jahon2 = News.published.all().filter(category__name='jahon').order_by("-publish_time")[1]
    jahon3 = News.published.all().filter(category__name='jahon').order_by("-publish_time")[2]
    jahon4 = News.published.all().filter(category__name='jahon').order_by("-publish_time")[3]
    jahon5 = News.published.all().filter(category__name='jahon').order_by("-publish_time")[4]
    jahon6 = News.published.all().filter(category__name='jahon').order_by("-publish_time")[5]
    jahon7 = News.published.all().filter(category__name='jahon').order_by("-publish_time")[6]
    jahon8 = News.published.all().filter(category__name='jahon').order_by("-publish_time")[7]
    jahon9 = News.published.all().filter(category__name='jahon').order_by("-publish_time")[8]
    jahon10 = News.published.all().filter(category__name='jahon').order_by("-publish_time")[9]

    context={
        "news_list":news_list,
        "categories":categories,
        "local_1":local_1,
        "local_2":local_2,
        "local_3": local_3,
        "local_4": local_4,
        "local_5": local_5,
        "sport_1":sport_1,
        "sport_2":sport_2,
        "sport_3":sport_3,
        "sport_4":sport_4,
        "jahon_one":jahon_one,
        "fan_texnika1":fan_texnika1,
        "fan_texnika2": fan_texnika2,
        "fan_texnika3": fan_texnika3,
        "fan_texnika4": fan_texnika4,
        "jahon1":jahon1,
        "jahon2": jahon2,
        "jahon3": jahon3,
        "jahon4": jahon4,
        "jahon5": jahon5,
        "jahon6": jahon6,
        "jahon7": jahon7,
        "jahon8": jahon8,
        "jahon9": jahon9,
        "jahon10": jahon10,

    }
    return render(request, "news/index.html",context)


def UzbekistanPage(request):
    local_1 = News.published.all().filter(category__name="Uzbekistan").order_by("-publish_time")[0]
    local_2 = News.published.all().filter(category__name="Uzbekistan").order_by("-publish_time")[1]
    local_3 = News.published.all().filter(category__name="Uzbekistan").order_by("-publish_time")[2]
    local_4 = News.published.all().filter(category__name="Uzbekistan").order_by("-publish_time")[3]
    local_5 = News.published.all().filter(category__name="Uzbekistan").order_by("-publish_time")[4]
    local_6 = News.published.all().filter(category__name="Uzbekistan").order_by("-publish_time")[5]
    local_7 = News.published.all().filter(category__name="Uzbekistan").order_by("-publish_time")[6]
    local_8 = News.published.all().filter(category__name="Uzbekistan").order_by("-publish_time")[7]
    local_9 = News.published.all().filter(category__name="Uzbekistan").order_by("-publish_time")[8]
    local_10 = News.published.all().filter(category__name="Uzbekistan").order_by("-publish_time")[9]

    context = {
        "local_1": local_1,
        "local_2": local_2,
        "local_3": local_3,
        "local_4": local_4,
        "local_5": local_5,
        "local_6": local_6,
        "local_7": local_7,
        "local_8": local_8,
        "local_9": local_9,
        "local_10": local_10,
    }
    return render(request, 'news/uzbekistan.html',context)


def SportPage(request):
    local_1 = News.published.all().filter(category__name="sport").order_by("-publish_time")[0]
    local_2 = News.published.all().filter(category__name="sport").order_by("-publish_time")[1]
    local_3 = News.published.all().filter(category__name="sport").order_by("-publish_time")[2]
    local_4 = News.published.all().filter(category__name="sport").order_by("-publish_time")[3]
    local_5 = News.published.all().filter(category__name="sport").order_by("-publish_time")[4]
    local_6 = News.published.all().filter(category__name="sport").order_by("-publish_time")[5]
    local_7 = News.published.all().filter(category__name="sport").order_by("-publish_time")[6]
    local_8 = News.published.all().filter(category__name="sport").order_by("-publish_time")[7]
    local_9 = News.published.all().filter(category__name="sport").order_by("-publish_time")[8]
    local_10 = News.published.all().filter(category__name="sport").order_by("-publish_time")[9]

    context = {
        "local_1": local_1,
        "local_2": local_2,
        "local_3": local_3,
        "local_4": local_4,
        "local_5": local_5,
        "local_6": local_6,
        "local_7": local_7,
        "local_8": local_8,
        "local_9": local_9,
        "local_10": local_10,


    }
    return render(request, 'news/category.html',context)