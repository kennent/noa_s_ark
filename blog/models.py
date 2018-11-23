from django.db import models

class Illust(models.Model):
    title = models.CharField(max_length=200) # 제목
    char = models.CharField(max_length=200) # 캐릭터
    org = models.CharField(max_length=200) # 원본
    artist = models.CharField(max_length=200) # 아티스트
    tag = models.CharField(max_length=200) # 태그 ,로 slide하고 trim
    img = models.ImageField(upload_to='img') # 이미지
    
    # Create your models here. 