from django.db import models
from user.models import UserModel


# Create your models here.
class Post(models.Model):  # 새로운 모델을 생성
    class Meta:
        db_table = "post"

    title = models.CharField("제목",max_length=50)
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    content = models.CharField("내용",max_length=225)
    create_at = models.DateTimeField("작성시간",auto_now_add=True)
    update_at = models.DateTimeField("수정시간",auto_now=True)