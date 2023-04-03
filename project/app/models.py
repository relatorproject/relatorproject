from django.db import models

# Create your models here.
class Relator(models.Model):
  price = models.IntegerField(verbose_name="販売価格")
  location = models.CharField(max_length=50,verbose_name="所在地")
  planOfHouse = models.CharField(max_length=5,verbose_name="間取り")
  freedom = models.TextField(verbose_name="その他の情報",blank=True,null=True)
  image1 = models.ImageField(verbose_name='イメージ1',blank=True,null=True,upload_to="images")
  image2 = models.ImageField(verbose_name='イメージ1',blank=True,null=True,upload_to="images")
  image3 = models.ImageField(verbose_name='イメージ1',blank=True,null=True,upload_to="images")
  image4 = models.ImageField(verbose_name='イメージ1',blank=True,null=True,upload_to="images")
  image5 = models.ImageField(verbose_name='イメージ1',blank=True,null=True,upload_to="images")

  def __str__(self):
      return f"{self.price} {self.location} {self.planOfHouse} {self.image1}"

class Tweet(models.Model):
  title = models.CharField(max_length=100,verbose_name="タイトル")
  text = models.TextField(verbose_name="テキスト")
  file = models.FileField(verbose_name='ファイル',blank=True,null=True,upload_to="images")
  created_at = models.DateTimeField(auto_now_add=True)

class Favorite(models.Model):
   user = models.CharField(max_length=100,verbose_name="ユーザー")
   favorite_relator = models.ForeignKey(Relator,on_delete=models.CASCADE,verbose_name="お気に入りの物件")
   

