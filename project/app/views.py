from django.core import serializers
from rest_framework import generics
from .models import Relator,Tweet,Favorite
from rest_framework import viewsets
from .serializers import RelatorSerializer,TweetSerializer,FavoriteSerializer
#from . ownpermissions import ProfilePermission
from rest_framework.response import Response
from django.db.models import Q
import json
from django.http import HttpResponse
from django.http import JsonResponse
import json
class RelatorViewSet(viewsets.ModelViewSet):#ModelViewSetを継承することでCRUDの動きに対応できる。
  queryset = Relator.objects.order_by('-id')#タスクオブジェクトの値をすべて取得する
  serializer_class = RelatorSerializer#TaskSerializerのクラスを使用する
  #authentication_classes = (TokenAuthentication,)#ユーザー認証を使うためにTokenAuthenticationを使う？
  #
  #permission_classes = (IsAuthenticated,)#認証しているユーザーのみアクセス許可を与える
  #permission_classes = (AllowAny)
class TweetViewSet(viewsets.ModelViewSet):
  queryset = Tweet.objects.order_by('-id')
  serializer_class = TweetSerializer
  
class RelatorSearch(viewsets.ModelViewSet):
  queryset = Tweet.objects.order_by('-id')
  serializer_class = TweetSerializer

class RelatorSearchViewSet(generics.ListAPIView):#単一のモデルを読み取りまたは更新したい時に使う。
  serializer_class = RelatorSerializer#UserSerializerのクラスを使用する
  queryset = Relator.objects.all().order_by('-id')
  def get_queryset(self):#フロントからGET通信を受け取ったので値を返す
    result = Relator.objects.all().order_by('-id')
    location = self.request.GET.get('location')
    priceSearch = self.request.GET.get('price')
    id_search = self.request.GET.get('id')
    if(location):
      search = result.filter(Q(location__icontains = location))
      if(priceSearch):
        return search.filter(price__lte = priceSearch)
      else:
        return search
    elif(id_search):
      print(id_search)
      return result.filter(Q(id = id_search))
    else:
      return result
    
    
    #return Relator.objects.order_by('-id').filter(location_icontains = self.request.location)#リクエストユーザーの情報を返す。

class FavoriteViewSet(viewsets.ModelViewSet):
   queryset = Favorite.objects.order_by('-id')
   serializer_class = FavoriteSerializer

   def get_queryset(self):#フロントからGET通信を受け取ったので値を返す
    result = Favorite.objects.order_by('-id')
    email = self.request.GET.get('favorite')
    if(email):
      return result.filter(Q(user = email))
    else:
      return result
    #return Relator.objects.order_by('-id').filter(location_icontains = self.request.location)#リクエストユーザーの情報を返す

#クライアントからのGetメソッドに対して値を返す
def testView(request):

  #モデルのquerysetオブジェクトから指定したプロパティの値を取り出しリストにする。
  test = Relator.objects.all().values_list('pk',flat=True)
  number = list(test)
  #モデルのquerysetオブジェクトから指定したプロパティの値を取り出しリストにする。
  
  #シリアライズのためjavascriptのオブジェクト記述をする。
  name = {
    
      "pokemon":number
    
  }
  #シリアライズのためjavascriptのオブジェクト記述をする。

  #シリアライズしてクライアントにレスポンスする。
  return JsonResponse(name,safe=False);
  #シリアライズしてクライアントにレスポンスする。
  


 
