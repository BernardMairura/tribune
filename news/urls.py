from django.urls import path,re_path
from .import views
from django.conf import settings
from django.conf.urls.static import static
# from news.views import logout_view



urlpatterns=[ 
   
    path('',views.news_today,name='newsToday'),
    path('search/', views.search_results, name='search_results'),
    re_path(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_news,name = 'pastNews'),
    # path('article/<int:article_id>',views.article,name ='article'),
    re_path(r'^new/article$', views.new_article, name='new-article'),
    re_path(r'article/(\d+)', views.article, name='article'),
    re_path(r'^ajax/newsletter/$', views.newsletter, name='newsletter'),
    re_path(r'^api/merch/$', views.MerchList.as_view())
   
]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)