from django.urls import path,include
from rest_framework import routers
from .views import RelatorViewSet,TweetViewSet,RelatorSearchViewSet,FavoriteViewSet,testView

router = routers.DefaultRouter()
router.register('relator',RelatorViewSet)
router.register('tweet',TweetViewSet)
router.register('favorite',FavoriteViewSet)


urlpatterns = [
    path('',include(router.urls)),#routerのurlを割り当てて対応したクラスを呼び出す
     path('relator_search/', RelatorSearchViewSet.as_view(),name="relator_search"),#genericsを継承したクラスのViewはroutersを使わない方法で取ってくる。
    path('test/',testView,name='test'),#routerのurlを割り当てて対応したクラスを呼び出す
]
