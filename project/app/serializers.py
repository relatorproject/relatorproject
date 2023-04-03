from rest_framework import serializers
from .models import Relator,Tweet,Favorite
from django.contrib.auth.models import User
from django.utils.timesince import timesince


class TweetSerializer(serializers.ModelSerializer):
  created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", read_only=True)
  class Meta:
    model = Tweet
    fields = ['id','title','created_at','text','file']

class FavoriteSerializer(serializers.ModelSerializer):
  #favorite_relator = serializers.StringRelatedField()
  class Meta:
    model = Favorite
    fields = ['id','user','favorite_relator']

class RelatorSerializer(serializers.ModelSerializer):
  favorite = FavoriteSerializer
  class Meta:
    model = Relator
    #fields = ['id','price','location','planOfHouse','freedom','image1','image2','image3','image4','image5']
    fields = "__all__"